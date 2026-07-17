# CT200 Document Management System

This project was developed as part of the AI Engineering Internship assignment. The objective was to build a backend system capable of parsing technical PDF documents, reconstructing their hierarchy, maintaining multiple document versions, and generating AI-powered question-answer pairs from selected sections.

The application is built using FastAPI and follows a modular architecture where each component is responsible for a single stage of the document lifecycle—from PDF parsing to AI content generation.

---

## What the system does

Instead of treating a PDF as plain text, the application reconstructs its logical structure by identifying numbered headings and building a hierarchy of sections and subsections.

Once parsed, the document is stored in SQLite with complete parent-child relationships, allowing the document to be browsed through REST APIs.

The system also supports multiple versions of the same document. Whenever a new version is uploaded, section hashes are compared to identify additions, removals and modifications.

Users can create selections consisting of multiple document nodes. These selections are passed to Google Gemini to automatically generate question-answer pairs. Every generated response is stored in MongoDB together with metadata such as node hashes, timestamps and version information. During retrieval, the stored hashes are compared against the latest document version to determine whether the generated content is stale.

---

## Tech Stack

| Layer | Technology |
|--------|------------|
| Backend | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite |
| AI | Google Gemini |
| NoSQL | MongoDB |
| PDF Parsing | PyMuPDF |
| Testing | Pytest |

---

## Project Structure

```
app
│
├── api
├── database
├── models
├── parser
├── schemas
├── services
│
tests
│
data
```

The project follows a layered architecture where APIs remain lightweight while most of the business logic resides inside the service layer.

---

## Setting up the project

Clone the repository

```bash
git clone <repository-url>
cd CT200-Document-Management-System
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
MONGODB_URI=mongodb://localhost:27017/
```

Run the application

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Project Workflow

The application processes a document through the following stages:

```
PDF Upload
      │
      ▼
Extract Text Blocks
      │
      ▼
Build Hierarchical Tree
      │
      ▼
Store in SQLite
      │
      ▼
Browse Document
      │
      ▼
Compare Versions
      │
      ▼
Create Selection
      │
      ▼
Generate QA using Gemini
      │
      ▼
Store in MongoDB
      │
      ▼
Retrieve & Check Staleness
```

---

## APIs

The backend exposes APIs for document upload, browsing, version comparison, selection management and AI-generated content retrieval.

Some of the primary endpoints include:

| Method | Endpoint |
|--------|----------|
| POST | `/api/documents/upload` |
| GET | `/api/browse/{document_id}` |
| GET | `/api/compare/{version1}/{version2}` |
| POST | `/api/selections` |
| POST | `/api/selections/{id}/generate-qa` |
| GET | `/api/generated/{selection_id}` |
| GET | `/api/generated/node/{node_id}` |

---

## Testing

Parser behaviour has been validated using Pytest.

The tests cover scenarios such as:

- nested document hierarchies
- duplicate headings
- ignored preface text
- paragraph merging
- heading identification
- complex parent-child relationships

Run the tests using

```bash
pytest
```

or

```bash
pytest tests/test_hierarchy_builder.py -v
```

---

## Design Decisions

A few implementation choices made during development:

- SQLite was used for structured document storage because of its simplicity and lightweight setup.
- MongoDB was chosen for AI-generated responses since the generated data has a flexible schema.
- SHA-256 hashes are used to detect section-level modifications between document versions.
- Google Gemini is integrated only after a user explicitly creates a selection, reducing unnecessary API usage.
- The parser reconstructs hierarchy using a stack-based approach instead of relying on indentation or font size alone.

---

## Future Improvements

Some improvements that could be added in future iterations include semantic search, vector embeddings, authentication, document summarization and a web-based frontend.

---

Developed as part of the **CT200 AI Engineering Internship Assignment**.