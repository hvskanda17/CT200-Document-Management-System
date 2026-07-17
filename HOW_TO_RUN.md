# Running the CT200 Document Management System

## Prerequisites

Before running the project, ensure the following are installed:

- Python 3.11 or later
- MongoDB Community Server
- Git
- Visual Studio Code (recommended)

---

## Clone the Repository

```bash
git clone <repository-url>
cd CT200-Document-Management-System
```

---

## Create a Virtual Environment

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
MONGODB_URI=mongodb://localhost:27017/
```

---

## Start MongoDB

Make sure the MongoDB service is running before starting the application.

Default connection:

```
mongodb://localhost:27017/
```

---

## Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

The application starts at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

# Project Execution Flow

## 1. Upload a PDF

Upload the first version of the CT200 manual using the document upload endpoint.

The PDF will be:

- Parsed
- Converted into a hierarchy
- Stored in SQLite

---

## 2. Browse the Document

Use the browse endpoint to verify that the hierarchy has been created successfully.

---

## 3. Upload Another Version

Upload a modified version of the same document.

A new version entry will be created.

---

## 4. Compare Versions

Use the version comparison endpoint.

The API returns:

- Added sections
- Removed sections
- Modified sections
- Unchanged sections

---

## 5. Create a Selection

Create a selection by providing the required node IDs.

Example:

```json
{
    "version_id": 1,
    "node_ids": [10,18,25]
}
```

---

## 6. Generate Question-Answer Pairs

Call:

```
POST /api/selections/{selection_id}/generate-qa
```

The selected content is sent to Google Gemini.

The generated questions are stored in MongoDB.

---

## 7. Retrieve Generated QA

Retrieve QA using:

```
GET /api/generated/{selection_id}
```

The response also indicates whether the generated content is stale.

---

## 8. Retrieve QA by Node

Retrieve every generated QA associated with a document node.

```
GET /api/generated/node/{node_id}
```

---

## Running Tests

Execute all unit tests:

```bash
pytest
```

Run only the parser tests:

```bash
pytest tests/test_hierarchy_builder.py -v
```

---

## Project Completion

If all APIs execute successfully and the unit tests pass, the project has been set up correctly and is ready for use.