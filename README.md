# Recruitment & Placement Management System - Python VS Code Project

Student-friendly Python + MySQL starter project.

## Open in VS Code

1. Extract the ZIP.
2. VS Code -> File -> Open Folder.
3. Select `RPMS_Python_VSCode`.
4. Open Terminal.
5. Run:

```bash
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

6. Check MySQL credentials in:

`rpms/util/db_connection.py`

7. Run:

```bash
python main.py
```

The project is configured for the MySQL database `recruitment_portal`.

## Included

- Candidate model, DAO and service
- Job DAO
- Application DAO and service
- Eligibility engine
- Custom exceptions
- MySQL connectivity
- Validation helpers
- File activity logging
- Basic report
- Console menu
- SQL schema/sample/full setup scripts
- VS Code run/debug configuration

Students can extend Company, Interview, Offer, Placement and additional reports.


## Recent Enhancements
- Updated menu labels and prompts for better readability
- Added full name and passing year validations
- Added Search Candidates by Technology (Option 6)
- Added Filter Candidates by Placement Status (Option 7)
- Added total record count summaries for candidates and open jobs