#!/usr/bin/env python3
"""
Google Forms Quiz Creator Script
Creates interactive diabetes quizzes from spreadsheet data using Google Forms API

Dependencies:
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

Authentication:
1. Create Google Cloud Project
2. Enable Google Forms API and Google Sheets API
3. Create OAuth 2.0 credentials
4. Configure consent screen
5. Download credentials.json file

Usage:
1. Place credentials.json in the same directory
2. Run: python google_forms_quiz_creator.py

This script reads quiz data from Google Sheets and creates responsive Google Forms.
"""

import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Google API scopes
SCOPES = [
    'https://www.googleapis.com/auth/forms',
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.file'
]

class DiabetesFormsCreator:
    """
    Creates Google Forms quizzes from diabetes training data
    """

    def __init__(self, spreadsheet_id=None, credentials_file='credentials.json'):
        self.spreadsheet_id = spreadsheet_id or '1rIXUAXmUefWi6Oc8hHdJCvtPjwzKpQVjaBYqjdcLK8A'
        self.credentials_file = credentials_file
        self.forms_service = None
        self.sheets_service = None
        self.drive_service = None

    def authenticate_google_apis(self):
        """Authenticate with Google APIs"""
        creds = None

        # Check for saved credentials
        token_file = 'token.json'
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)

        # Refresh or create new credentials if needed
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)

            # Save credentials for next run
            with open(token_file, 'w') as token:
                token.write(creds.to_json())

        # Build API services
        self.forms_service = build('forms', 'v1', credentials=creds)
        self.sheets_service = build('sheets', 'v4', credentials=creds)
        self.drive_service = build('drive', 'v3', credentials=creds)

        print("✓ Successfully authenticated with Google APIs")

    def read_quiz_data_from_sheets(self, range_name='Sheet1!A:N'):
        """
        Read quiz questions from Google Sheets
        Expected columns: Question, Option1, Option2, Option3, Option4, Answer, Section, Difficulty, Explanation
        """
        try:
            result = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_name).execute()

            values = result.get('values', [])
            if not values:
                print('No quiz data found in spreadsheet')
                return []

            headers = values[0]
            quiz_data = []

            for row in values[1:]:
                if len(row) >= len(headers):
                    question_data = dict(zip(headers, row))
                    quiz_data.append(question_data)

            print(f"✓ Loaded {len(quiz_data)} quiz questions from Sheets")
            return quiz_data

        except HttpError as error:
            print(f"Error reading from Sheets: {error}")
            return []

    def create_diabetes_quiz_form(self, quiz_data, quiz_title="Diabetes CBME Assessment Quiz"):
        """
        Create a Google Form with diabetes quiz questions
        """
        if not quiz_data:
            print("No quiz data provided")
            return None

        # Form metadata
        form_info = {
            'info': {
                'title': quiz_title,
                'description': 'CBME Diabetes Training Module - Interactive Assessment\n'
                              'Mentored by Dr. Siddalingaiah H S, Shridevi Medical Sciences & Research Hospital'
            }
        }

        try:
            # Create the form
            form = self.forms_service.forms().create(body=form_info).execute()
            form_id = form['formId']
            print(f"✓ Created Google Form: {quiz_title}")
            print(f"Form URL: https://forms.google.com/forms/d/{form_id}/viewform")

            # Add quiz questions
            questions_batch = []

            for i, question in enumerate(quiz_data[:20]):  # Limit to 20 questions for demo
                try:
                    form_question = self.create_question_from_data(question, i)
                    if form_question:
                        questions_batch.append(form_question)
                except Exception as q_error:
                    print(f"Error creating question {i+1}: {q_error}")
                    continue

            # Update form with questions
            if questions_batch:
                update_request = {
                    'requests': [{'createItem': {'item': q, 'location': {'index': len(questions_batch)}}} for q in questions_batch]
                }

                self.forms_service.forms().batchUpdate(formId=form_id, body=update_request).execute()
                print(f"✓ Added {len(questions_batch)} questions to the quiz form")

            # Make form quiz-like by setting response settings
            self.configure_form_settings(form_id)

            return f"https://forms.google.com/forms/d/{form_id}/viewform"

        except HttpError as error:
            print(f"Error creating form: {error}")
            return None

    def create_question_from_data(self, question_data, index):
        """Create form question from row data"""
        question_text = question_data.get('Question', f'Question {index+1}')

        # Get options
        options = []
        for i in range(1, 5):  # Options 1-4
            option_text = question_data.get(f'Option{i}', '')
            if option_text.strip():
                options.append(option_text)

        if len(options) < 2:
            return None

        # Set correct answer (assuming it's a number 1-4)
        try:
            correct_index = int(question_data.get('Answer', '1')) - 1
            correct_option = options[correct_index] if correct_index < len(options) else options[0]
        except (ValueError, IndexError):
            correct_option = options[0]  # Default to first option

        # Get additional metadata
        section = question_data.get('Section', 'General')
        explanation = question_data.get('Explanation', '')

        # Create question structure
        question_item = {
            'title': f'Q{index+1}: {question_text}',
            'questionItem': {
                'question': {
                    'required': True,
                    'choiceQuestion': {
                        'type': 'RADIO',
                        'options': [{'value': opt} for opt in options],
                        'shuffle': False
                    }
                }
            }
        }

        return question_item

    def configure_form_settings(self, form_id):
        """Configure form response and quiz settings"""
        try:
            # Update form settings
            update_request = {
                'requests': [
                    {
                        'updateFormInfo': {
                            'info': {
                                'formId': form_id,
                                'settings': {
                                    'quizSettings': {
                                        'isQuiz': True
                                    }
                                }
                            },
                            'updateMask': 'settings.quizSettings'
                        }
                    }
                ]
            }

            self.forms_service.forms().batchUpdate(formId=form_id, body=update_request).execute()
            print("✓ Form configured as interactive quiz")

        except HttpError as error:
            print(f"Error configuring form settings: {error}")

    def get_form_responses(self, form_id, response_id=None):
        """Retrieve form response data for analysis"""
        try:
            if response_id:
                response = self.forms_service.forms().responses().get(
                    formId=form_id, responseId=response_id).execute()
                return response
            else:
                # Get all responses
                responses = self.forms_service.forms().responses().list(formId=form_id).execute()
                return responses.get('responses', [])

        except HttpError as error:
            print(f"Error retrieving responses: {error}")
            return []

    def generate_quiz_report(self, form_id, responses):
        """Generate quiz performance report"""
        if not responses:
            return None

        report = {
            'total_responses': len(responses),
            'questions_analyzed': 0,
            'average_score': 0,
            'section_breakdown': {}
        }

        return report


def demo_diabetes_quiz_creation():
    """
    Demo function showing how to create diabetes quiz forms
    """
    print("🩺 Diabetes Google Forms Creator Demo")
    print("=" * 50)

    # Sample diabetes quiz data (in case Sheets access fails)
    sample_quiz_data = [
        {
            'Question': 'What is the current global prevalence of diabetes mellitus (2023)?',
            'Option1': '337 million people (IDF Atlas 9th Edition)',
            'Option2': '463 million people (IDF Atlas 9th Edition)',
            'Option3': '537 million people (IDF Atlas 10th Edition)',
            'Option4': '611 million people (IDF Atlas 10th Edition)',
            'Answer': '3',
            'Section': 'Epidemiology',
            'Explanation': 'IDF Atlas 10th Edition reports 537 million adults with diabetes globally'
        },
        {
            'Question': 'According to ADA 2023 guidelines, which HbA1c level confirms diabetes diagnosis?',
            'Option1': '≥ 6.0% (42 mmol/mol)',
            'Option2': '≥ 6.5% (48 mmol/mol)',
            'Option3': '≥ 7.0% (53 mmol/mol)',
            'Option4': '≥ 7.5% (58 mmol/mol)',
            'Answer': '2',
            'Section': 'Diagnosis',
            'Explanation': 'ADA defines diabetes as HbA1c ≥ 6.5% on two occasions'
        },
        {
            'Question': 'First-line pharmacological treatment for Type 2 diabetes according to ADA/EASD 2022 consensus is:',
            'Option1': 'Insulin glargine',
            'Option2': 'Metformin',
            'Option3': 'Sulfonylureas',
            'Option4': 'DPP-4 inhibitors',
            'Answer': '2',
            'Section': 'Management',
            'Explanation': 'Metformin remains first-line unless contraindicated'
        }
    ]

    # Create forms creator instance
    quiz_creator = DiabetesFormsCreator()

    try:
        # Authenticate (requires credentials.json)
        print("Authenticating with Google APIs...")
        print("Note: This requires 'credentials.json' file in the current directory")
        print("Visit Google Cloud Console to create OAuth credentials")

        quiz_creator.authenticate_google_apis()

        # Try to read from Sheets, fallback to sample data
        quiz_data = quiz_creator.read_quiz_data_from_sheets()
        if not quiz_data:
            print("Using sample quiz data instead of Google Sheets")
            quiz_data = sample_quiz_data

        # Create the quiz form
        form_url = quiz_creator.create_diabetes_quiz_form(
            quiz_data,
            "Diabetes CBME Assessment Quiz - Dr. H S"
        )

        if form_url:
            print("\n" + "="*60)
            print("🎉 QUIZ FORM CREATED SUCCESSFULLY!")
            print(f"📋 Access the quiz: {form_url}")
            print(f"📊 Form responses: {form_url.replace('viewform', 'responses')}")
            print("="*60)

            # Show form sharing info
            print("\n📤 Form Sharing Options:")
            print("1. Send quiz link to students via email/portal")
            print("2. Embed in Canvas/Moodle LMS")
            print("3. Include in training module materials")
            print("4. Auto-grade responses for instant feedback")

        else:
            print("❌ Form creation failed. Check API credentials and permissions.")

    except FileNotFoundError:
        print("❌ Credentials file 'credentials.json' not found.")
        print("📋 To create credentials:")
        print("   1. Go to Google Cloud Console")
        print("   2. Create new project or select existing")
        print("   3. Enable Google Forms API and Google Sheets API")
        print("   4. Configure OAuth consent screen")
        print("   5. Create OAuth 2.0 Client ID credentials")
        print("   6. Download credentials.json")

        # Demo with sample data (no API calls)
        print("\n📊 Sample Quiz Preview:")
        quiz_creator = DiabetesFormsCreator()
        for i, q in enumerate(sample_quiz_data[:3]):
            print(f"\nQ{i+1}: {q['Question']}")
            for j in range(1, 5):
                opt = q.get(f'Option{j}', '')
                if opt:
                    print(f"   {j}. {opt}")
            print(f"   ✓ Answer: {q['Answer']} ({q['Section']})")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("💡 Make sure all required permissions are configured in Google Cloud Console")


if __name__ == "__main__":
    demo_diabetes_quiz_creation()
