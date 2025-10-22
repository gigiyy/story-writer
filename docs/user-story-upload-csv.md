
# User Story: Upload CSV and Validate Records
As a user, I want to upload a CSV file through a web interface so that the application can read its content, validate each row based on configurable rules, and display a summary table of accepted, rejected, and total records directly below the upload form.


## Acceptance Criteria
```gherkin
Scenario: Uploading a valid CSV file
  Given I have a CSV file formatted according to the application's requirements
  When I upload the file through the web interface
  Then the application should process each row and apply validation rules:
    | Rule                        | Description                                 |
    |-----------------------------|---------------------------------------------|
    | TRANSACTION_AMOUNT positive | Each amount must be greater than 0          |
    | TRANSACTION_ID unique       | Each ID must be unique within the file      |
  And I should see a summary table below the upload form showing the number of accepted, rejected, and total records

Scenario: Uploading a CSV file with invalid rows
  Given my CSV file contains some rows that do not meet the validation criteria
  When I upload the file
  Then the application should reject those rows
  And the summary table should accurately reflect the count of accepted and rejected records

Scenario: Uploading an empty or malformed CSV file
  Given I upload an empty or incorrectly formatted CSV file
  When the application processes the file
  Then I should receive an error message indicating the issue
  And no records should be processed

Scenario: Table output format
  Given I upload a CSV file
  When the file is processed
  Then the summary table should display headers "Accepted", "Rejected", "Total" and a row with the corresponding numbers in order

Scenario: API request for CSV upload
  Given I send a POST request with a CSV file to the /aml/upload_csv endpoint
  When the request is accepted
  Then the response should be in JSON format with accepted, rejected, and total record counts
```


## Notes
- The web UI is accessible at `/aml/upload_csv` and displays results in a table below the upload form after submission.
- The endpoint supports both browser form submissions (HTML response) and API requests (JSON response).
- Input validation checks for required columns, data types, and business-specific rules:
  - `TRANSACTION_AMOUNT` must be greater than 0
  - `TRANSACTION_ID` must be unique within the file
- Validation rules are modular and can be extended for future requirements.
- Performance should be considered for large files; consider streaming or chunked processing.
- Edge cases include empty files, files with only invalid rows, and files with mixed valid/invalid rows.
- The result summary is clear and accessible to both technical and non-technical users.
- Rules can be applied selectively by modifying configuration code.
- Sample CSV file in `data/sample.csv`.
