# Decision Log

## 1. FastAPI as the Backend Framework

FastAPI was chosen because it provides automatic API documentation, type validation using Pydantic, and a clean structure for building REST APIs.

---

## 2. SQLite for Structured Data

SQLite was used to store documents, versions, hierarchy nodes, and selections. It is lightweight, easy to set up, and suitable for this assignment.

---

## 3. MongoDB for AI-Generated Content

Generated question-answer pairs were stored in MongoDB because the structure of AI responses is flexible and can evolve without schema changes.

---

## 4. Stack-Based Hierarchy Construction

A stack-based approach was used to reconstruct the document hierarchy from numbered headings. This allows efficient parent-child relationship creation without multiple passes through the document.

---

## 5. SHA-256 Content Hashing

Each node stores a SHA-256 hash of its content. Comparing hashes across versions makes it easy to detect added, modified, and unchanged sections.

---

## 6. Selection-Based QA Generation

Instead of generating QA for an entire document, users first create a selection of relevant nodes. This reduces unnecessary API calls and focuses the generated content.

---

## 7. Staleness Detection

The hashes stored with generated QA are compared against the latest document hashes during retrieval. If differences are found, the generated content is marked as stale instead of being regenerated automatically.