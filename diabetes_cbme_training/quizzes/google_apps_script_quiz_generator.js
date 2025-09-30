/**
 * Google Apps Script - Quiz Form Generator from Sheets
 *
 * This script reads quiz data from Google Sheets and automatically creates
 * a Google Forms quiz. To use:
 *
 * 1. Open your Google Sheet (https://docs.google.com/spreadsheets/d/SPREADSHEET_ID)
 * 2. Click Extensions > Apps Script
 * 3. Paste this entire script
 * 4. Save the script
 * 5. Run the createDiabetesQuiz function
 *
 * Expected Sheet structure (Sheet called "QuizData"):
 * Column A: Question
 * Column B: Option1
 * Column C: Option2
 * Column D: Option3
 * Column E: Option4
 * Column F: Answer (number 1-4)
 * Column G: Section (optional)
 * Column H: Explanation (optional)
 */

/**
 * Main function to create diabetes quiz form
 */
function createDiabetesQuiz() {
  try {
    var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = spreadsheet.getSheetByName('QuizData');

    if (!sheet) {
      Logger.log("Error: No sheet named 'QuizData' found. Please create it with quiz data.");
      showUserMessage("Error: No sheet named 'QuizData' found. Please create it with quiz data.");
      return;
    }

    // Get quiz data
    var data = sheet.getDataRange().getValues();
    if (data.length < 2) {
      Logger.log("Error: No quiz questions found. Please add questions to Sheet1.");
      showUserMessage("Error: No quiz questions found. Please add questions to the sheet.");
      return;
    }

    // Create the form
    var formTitle = "Diabetes CBME Assessment Quiz - " + new Date().toLocaleDateString();
    var formDescription = "CBME Diabetes Training Module - Interactive Assessment\\n\\n" +
                         "Mentored by Dr. Siddalingaiah H S\\n" +
                         "Shridevi Institute of Medical Sciences & Research Hospital";

    var form = FormApp.create(formTitle);
    form.setDescription(formDescription);

    // Set basic form settings (limited methods available in Apps Script)
    try {
      form.setIsQuiz(true);
    } catch(e) {
      Logger.log("Quiz settings not fully supported in this context");
    }

    // Skip header row
    for (var i = 1; i < data.length; i++) {
      var row = data[i];
      if (!row[0] || row[0].trim() === '') continue; // Skip empty rows

      var questionText = row[0];
      var option1 = row[1] || '';
      var option2 = row[2] || '';
      var option3 = row[3] || '';
      var option4 = row[4] || '';
      var correctAnswerIndex = parseInt(row[5]) - 1; // Convert to 0-based index

      // Add section header if new section
      var section = row[6] || '';
      if (section) {
        try {
          var sectionItem = form.addPageBreakItem();
          sectionItem.setTitle(section);
        } catch(e) {
          // Skip if section headers not supported
        }
      }

      // Create the question
      var item = form.addMultipleChoiceItem();
      item.setTitle('Q' + (i) + ': ' + questionText);
      item.setChoiceValues([option1, option2, option3, option4])
          .setChoices([
            item.createChoice(option1, correctAnswerIndex === 0),
            item.createChoice(option2, correctAnswerIndex === 1),
            item.createChoice(option3, correctAnswerIndex === 2),
            item.createChoice(option4, correctAnswerIndex === 3)
          ]);

      // Set question settings
      item.setRequired(true);

      // Add explanation if provided
      var explanation = row[7] || '';
      if (explanation) {
        // Note: Apps Script may not support explanations directly
        // This could be enhanced with Google Forms API
      }
    }

    // Get form URL
    var formUrl = form.getPublishedUrl();
    Logger.log('Quiz form created successfully: ' + formUrl);

    // Show success message with form URL
    var message = '🎉 Diabetes Quiz Form Created Successfully!\n\n' +
                  '📋 Form Title: ' + formTitle + '\n' +
                  '🔗 Form URL: ' + formUrl + '\n\n' +
                  '📊 Edit Form: ' + form.getEditUrl() + '\n' +
                  '📈 View Responses: ' + form.getSummaryUrl();

    Browser.msgBox(message);

    // Return form URL for use in sheets
    return formUrl;

  } catch (error) {
    Logger.log('Error creating quiz form: ' + error.toString());
    showUserMessage('Error creating quiz form: ' + error.toString());
    return null;
  }
}

/**
 * Alternative function to create form from specific range
 */
function createQuizFromRange(rangeNotation) {
  try {
    var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    var range = spreadsheet.getRange(rangeNotation);
    var data = range.getValues();

    Logger.log('Creating quiz from range: ' + rangeNotation);
    return processQuizData(data);

  } catch (error) {
    Logger.log('Error creating quiz from range: ' + error.toString());
    return null;
  }
}

/**
 * Process quiz data and create form
 */
function processQuizData(data) {
  if (!data || data.length < 1) {
    throw new Error('No quiz data provided');
  }

  var formTitle = "Diabetes Training Quiz - " + new Date().toLocaleDateString();
  var form = FormApp.create(formTitle);
  form.setDescription("CBME Diabetes Assessment");
  form.setIsQuiz(true);

  // Add questions (skip header if present)
  var startRow = data[0][0] === 'Question' ? 1 : 0;

  for (var i = startRow; i < data.length; i++) {
    var row = data[i];
    if (!row[0] || row[0].trim() === '') continue;

    var questionText = row[0];
    var options = [
      row[1] || '',
      row[2] || '',
      row[3] || '',
      row[4] || ''
    ];
    var correctAnswerIndex = parseInt(row[5]) - 1;

    var item = form.addMultipleChoiceItem();
    item.setTitle(questionText);

    var choices = [];
    for (var j = 0; j < options.length; j++) {
      if (options[j]) {
        choices.push(item.createChoice(options[j], j === correctAnswerIndex));
      }
    }

    item.setChoiceValues(options)
        .setChoices(choices);
    item.setRequired(true);
  }

  return form.getPublishedUrl();
}

/**
 * Add custom menu to Google Sheets
 */
function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('🤖 Quiz Generator')
      .addItem('🎯 Create Diabetes Quiz', 'createDiabetesQuiz')
      .addItem('📊 Create Quiz from Range', 'showRangeDialog')
      .addSeparator()
      .addItem('📚 View Guide', 'showGuide')
      .addToUi();
}

/**
 * Show range selection dialog
 */
function showRangeDialog() {
  var html = HtmlService.createHtmlOutputFromFile('range_dialog.html')
      .setWidth(400)
      .setHeight(300);
  SpreadsheetApp.getUi().showModalDialog(html, 'Select Range for Quiz');
}

/**
 * Show usage guide
 */
function showGuide() {
  var guide = "🤖 Google Sheets Quiz Generator Guide\\n\\n" +
              "1. 📋 Setup your quiz data in sheet named 'QuizData'\\n" +
              "   - Column A: Question\\n" +
              "   - Columns B-E: Options (1-4)\\n" +
              "   - Column F: Answer (1-4)\\n" +
              "   - Column G: Section (optional)\\n" +
              "   - Column H: Explanation (optional)\\n\\n" +
              "2. 🎯 Click 'Create Diabetes Quiz' in the Quiz Generator menu\\n\\n" +
              "3. 🎉 Your quiz form will be created and the URL will be shown\\n\\n" +
              "Example Data Format:\\n" +
              "Question,Option1,Option2,Option3,Option4,Answer\\n" +
              "\"What is diabetes?\",\"Type 1\",\"Type 2\",\"Both\",\"None\",\"2\"\\n";

  Browser.msgBox(guide);
}

/**
 * Helper function to show user messages
 */
function showUserMessage(message) {
  SpreadsheetApp.getUi().alert(message);
}

/**
 * Function to get all available forms (for debugging)
 */
function listForms() {
  try {
    var forms = DriveApp.searchFiles('mimeType contains "application/vnd.google-apps.form"');
    var formList = [];

    while (forms.hasNext()) {
      var form = forms.next();
      formList.push(form.getName() + ': ' + form.getUrl());
    }

    return formList.join('\\n');

  } catch (error) {
    return 'Error listing forms: ' + error.toString();
  }
}

/**
 * Test function with sample data
 */
function testCreateSampleQuiz() {
  try {
    var sampleData = [
      ['Question', 'Option1', 'Option2', 'Option3', 'Option4', 'Answer', 'Section'],
      ['What is the current global prevalence of diabetes mellitus (2023)?',
       '337 million people',
       '463 million people',
       '537 million people',
       '611 million people',
       3,
       'Epidemiology'],
      ['According to ADA 2023 guidelines, which HbA1c level confirms diabetes diagnosis?',
       '≥ 6.0% (42 mmol/mol)',
       '≥ 6.5% (48 mmol/mol)',
       '≥ 7.0% (53 mmol/mol)',
       '≥ 7.5% (58 mmol/mol)',
       2,
       'Diagnosis']
    ];

    Logger.log("Creating sample quiz for testing...");
    var formUrl = processQuizData(sampleData);
    Logger.log("Sample quiz created: " + formUrl);
    return formUrl;

  } catch (error) {
    Logger.log("Error in test: " + error.toString());
    return null;
  }
}

/**
 * Batch create multiple quizzes from different sections
 */
function createMultipleQuizzes() {
  try {
    var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = spreadsheet.getSheetByName('QuizData');
    var data = sheet.getDataRange().getValues();

    // Group by section
    var sections = {};
    var headerSkipped = false;

    for (var i = 0; i < data.length; i++) {
      var row = data[i];
      if (!headerSkipped && row[0] === 'Question') {
        headerSkipped = true;
        continue;
      }

      var section = row[6] || 'General';
      if (!sections[section]) {
        sections[section] = [];
      }
      sections[section].push(row);
    }

    var results = {};
    for (var section in sections) {
      Logger.log("Creating quiz for section: " + section);
      var formUrl = createSectionQuiz(section, sections[section]);
      results[section] = formUrl;
    }

    // Show results
    var message = "Multiple Quizzes Created:\\n\\n";
    for (var section in results) {
      message += section + ": " + results[section] + "\\n";
    }

    Browser.msgBox(message);
    return results;

  } catch (error) {
    Logger.log("Error creating multiple quizzes: " + error.toString());
    return null;
  }
}

/**
 * Create quiz for specific section
 */
function createSectionQuiz(sectionName, sectionData) {
  try {
    var formTitle = "Diabetes Quiz - " + sectionName + " (" + new Date().toLocaleDateString() + ")";
    var form = FormApp.create(formTitle);
    form.setDescription("Diabetes Training - " + sectionName + " Module\nCBME Assessment");
    form.setIsQuiz(true);

    for (var i = 0; i < sectionData.length; i++) {
      var row = sectionData[i];
      var questionText = row[0];
      var options = [row[1], row[2], row[3], row[4]];
      var correctAnswerIndex = parseInt(row[5]) - 1;

      if (questionText && questionText.trim() !== '') {
        var item = form.addMultipleChoiceItem();
        item.setTitle('Q' + (i + 1) + ': ' + questionText);

        var choices = [];
        for (var j = 0; j < options.length; j++) {
          if (options[j]) {
            choices.push(item.createChoice(options[j], j === correctAnswerIndex));
          }
        }

        item.setChoiceValues(options)
            .setChoices(choices);
        item.setRequired(true);
      }
    }

    return form.getPublishedUrl();

  } catch (error) {
    Logger.log("Error creating section quiz: " + error.toString());
    return null;
  }
}

/**
 * Export quiz data as JSON (for backup/debugging)
 */
function exportQuizDataAsJson() {
  try {
    var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = spreadsheet.getSheetByName('QuizData');
    var data = sheet.getDataRange().getValues();

    var jsonData = JSON.stringify(data, null, 2);

    // Create a new file in Drive
    var fileName = 'quiz_data_backup_' + new Date().getTime() + '.json';
    var file = DriveApp.createFile(fileName, jsonData, MimeType.PLAIN_TEXT);

    Logger.log('Quiz data exported to: ' + file.getUrl());
    return file.getUrl();

  } catch (error) {
    Logger.log("Error exporting data: " + error.toString());
    return null;
  }
}

/**
 * Validate quiz data format
 */
function validateQuizData() {
  try {
    var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = spreadsheet.getSheetByName('QuizData');

    if (!sheet) {
      return "❌ No sheet named 'QuizData' found";
    }

    var data = sheet.getDataRange().getValues();
    var issues = [];

    // Check basic structure
    if (data.length < 2) {
      issues.push("❌ No quiz questions found");
      return issues.join("\\n");
    }

    // Validate header row
    if (data[0][0] !== 'Question' || data[0][1] !== 'Option1' || data[0][data[0].length - 1] !== 'Explanation') {
      issues.push("⚠️ Warning: Unexpected header format. Expected: Question, Option1-4, Answer, Section, Explanation");
    }

    // Validate question data
    var validQuestions = 0;
    for (var i = 1; i < data.length; i++) {
      var row = data[i];
      if (!row[0] || row[0].trim() === '') continue;

      if (!row[1] || !row[2]) {
        issues.push("⚠️ Question " + i + " missing option(s)");
        continue;
      }

      var answerIndex = parseInt(row[5]);
      if (isNaN(answerIndex) || answerIndex < 1 || answerIndex > 4) {
        issues.push("⚠️ Question " + i + " has invalid answer (should be 1-4)");
        continue;
      }

      validQuestions++;
    }

    if (validQuestions === 0) {
      issues.push("❌ No valid quiz questions found");
    } else {
      issues.push("✅ Found " + validQuestions + " valid quiz questions");
    }

    return issues.join("\\n");

  } catch (error) {
    return "❌ Validation error: " + error.toString();
  }
}

/**
 * Menu item to run validation
 */
function validateDataMenu() {
  var result = validateQuizData();
  Browser.msgBox(result);
}
