# ESG Data Extraction System

## 1. Executive Summary
This repository implements a **production-oriented ESG data extraction system** designed to extract predefined Environmental, Social, and Governance (ESG) indicators from large annual report PDFs. The system is optimized for **accuracy, auditability, and deterministic behavior**, rather than exploratory semantic search.

The solution uses **page-guided PDF extraction combined with controlled LLM-based parsing**, and produces a structured CSV output suitable for downstream analytics or regulatory reporting.

---

## 2. Scope and Objectives

### In Scope
- Extraction of predefined ESG indicators (E, S, G)
- Deterministic page-based PDF parsing
- Controlled use of LLMs for structured extraction
- Explicit handling of missing or unavailable values
- CSV export for downstream consumption

### Out of Scope
- Free-form document summarization
- Narrative or qualitative analysis
- Semantic search across unknown documents
- Real-time or streaming ingestion

---

## 3. Design Principles

1. **Determinism over Recall**  
   The system only extracts values when explicitly present.

2. **Auditability by Design**  
   Every extracted value can be traced back to a PDF page range.

3. **LLM as a Parser, Not a Source of Truth**  
   The LLM never infers or fabricates values.

4. **Graceful Failure**  
   Missing values are explicitly recorded as `Not found`.

---

## 4. High-Level System Architecture

```
┌──────────────────────────┐
│ Configuration Layer       │
│ (Indicators & Pages)      │
└───────────┬──────────────┘
            │
            ▼
┌──────────────────────────┐
│ PDF Extraction Layer      │
│ (Page-based text reader)  │
└───────────┬──────────────┘
            │
            ▼
┌──────────────────────────┐
│ Text Aggregation Layer    │
│ (Per company)             │
└───────────┬──────────────┘
            │
            ▼
┌──────────────────────────┐
│ LLM Parsing Layer         │
│ (Batch JSON extraction)   │
└───────────┬──────────────┘
            │
            ▼
┌──────────────────────────┐
│ Validation & Normalization│
│ (Null-safe, deterministic)│
└───────────┬──────────────┘
            │
            ▼
┌──────────────────────────┐
│ Persistence Layer         │
│ (SQLite)                  │
└───────────┬──────────────┘
            │
            ▼
┌──────────────────────────┐
│ Export Layer              │
│ (CSV)                     │
└──────────────────────────┘
```

---

## 5. Component Breakdown

### 5.1 Configuration Layer
- `config/pages.py`: Maps each company to its PDF path and indicator-specific page ranges
- `config/indicators.py`: Defines indicator metadata (name, category, ESRS mapping, units)

This layer externalizes business logic and avoids hard-coded assumptions.

---

### 5.2 PDF Extraction Layer
- Reads only predefined page ranges
- Avoids OCR and semantic search
- Produces deterministic text output

This design ensures repeatability and performance.

---

### 5.3 Text Aggregation Layer
- Aggregates extracted text per company
- Minimizes the number of LLM calls

---

### 5.4 LLM Parsing Layer
- Single batch prompt per company
- Strict JSON schema enforced
- No inference or estimation allowed

The LLM is treated as a **structured text parser**, not a reasoning engine.

---

### 5.5 Validation & Normalization Layer
- Validates JSON structure
- Normalizes units and values
- Explicitly marks missing data

---

### 5.6 Persistence Layer
- SQLite used for intermediate storage
- Enables re-export, debugging, and audit trails

---

### 5.7 Export Layer
- Produces flat CSV output
- One row per `(company, indicator)`

---

## 6. Data Flow

1. Load indicator and page configuration
2. Read relevant pages from PDF
3. Aggregate text per company
4. Invoke LLM for batch extraction
5. Validate and normalize results
6. Persist to SQLite
7. Export final CSV

---

## 7. Execution Instructions

```bash
uv run python -m src.main
```

Output:
```
output/extractions.csv
```

---

## 8. Rationale for Key Decisions

### Why ESG-focused?
ESG indicators are regulated, structured, and auditable, making them suitable for deterministic extraction pipelines.

### Why No Vector Database?
- Page locations are known
- Indicators are predefined
- Precision is prioritized over semantic recall

### Why Batch LLM Calls?
- Reduces latency and cost
- Ensures consistency across indicators

---

## 9. Known Limitations
- Image-based tables may not extract correctly
- Extraction quality depends on PDF text fidelity
- LLM output can still fail schema validation (handled safely)

---

## 10. Future Enhancements
- Table-aware parsing
- Confidence scoring heuristics
- Indicator-level fallback strategies
- Support for additional report types

---

## 11. Conclusion

This system demonstrates a **pragmatic, production-aligned approach** to ESG data extraction, balancing automation with reliability and auditability. It is intentionally conservative, making it suitable for regulated reporting environments.
