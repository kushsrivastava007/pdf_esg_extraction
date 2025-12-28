# AI-Powered CSRD Indicator Extraction System

## Overview

This project implements an **AI-powered data extraction system** that automatically extracts **20 predefined sustainability (ESG) indicators** from **CSRD-aligned sustainability reports** of three European banks:

- BBVA  
- Groupe BPCE  
- AIB Group  

The system processes large PDF reports, extracts structured indicator data using an LLM, stores results in a database, and exports a consolidated CSV for downstream analysis.

The solution is designed as a **pragmatic, production-oriented prototype**, built under strict time constraints, prioritizing **accuracy, traceability, and explainability** over over-engineering.

---

## Problem Statement

CSRD sustainability reports are:
- Large (400–1100+ pages)
- Inconsistently structured
- A mix of tables, narratives, and appendices

Manual extraction of ESG indicators is:
- Time-consuming
- Error-prone
- Not scalable

The goal of this system is to **automate structured extraction** of a fixed set of ESG indicators while:
- Avoiding hallucinations
- Preserving source traceability
- Clearly handling missing or ambiguous disclosures

---

## Key Design Decisions (and Why)

### 1. Indicator-Driven Extraction (Not Open-Ended QA)

Extraction is driven by a **fixed list of 20 predefined indicators**, not free-form questions.

**Why**
- Matches regulatory and client requirements
- Prevents scope creep
- Enables deterministic outputs
- Easier to validate and scale

Each indicator has:
- A clear definition
- Expected unit
- Explicit output schema

---

### 2. Page-Scoped PDF Processing

The system extracts text only from **predefined page ranges** relevant to each indicator.

**Why**
- Full-document processing increases hallucination risk
- Reduces token usage and cost
- Improves accuracy by limiting context

**Important**
Page ranges are treated as **configuration metadata**, not hard-coded logic.

This reflects a **Phase-1 production prototype**:
- Manual scoping for known reports
- Designed to be replaced by automated section detection later

---

### 3. LLM as a Controlled Extraction Component

The LLM is used only for **narrow, deterministic extraction**, not reasoning or summarization.

**The LLM does**
- Scan scoped text for one indicator
- Extract a value if explicitly stated
- Return `null` if not found
- Assign a confidence score
- Cite source page and section

**The LLM does NOT**
- Guess missing values
- Infer from unrelated data
- Perform cross-section calculations
- Search external sources

---

### 4. Strict Structured Output Contract

The LLM must return **JSON-only output** with a fixed schema:

```json
{
  "value": number | string | null,
  "unit": string,
  "confidence": 0.0–1.0,
  "source_page": number,
  "source_section": string,
  "notes": string
}
```

This prevents ambiguity and simplifies validation.

---

### 5. Confidence Scoring

Every extracted value includes a **confidence score** to reflect disclosure quality.

Typical interpretation:
- 0.8–0.95 → Explicit table value
- 0.5–0.7 → Narrative disclosure
- ≤ 0.4 → Not found or unclear

---

### 6. Store Everything (Including Missing Values)

Every `(company, indicator)` attempt is stored as a row, even if the value is missing.

**Why**
- Prevents silent failures
- Makes coverage gaps explicit
- Supports audit and reprocessing

Missing data is a **documented outcome**, not an error.

---

### 7. SQLite for Storage

SQLite is used as the database because it:
- Requires zero setup
- Is sufficient for prototype scale
- Is easy to inspect and export
- Demonstrates system thinking without operational overhead

---

### 8. CSV as the Primary Deliverable

CSV export is treated as the **final authoritative output**.

**Why**
- Easy to review and validate
- Compatible with analytics tools
- Explicitly required by the case study

---

## System Architecture (Conceptual)

PDF Reports  
↓  
Page-Scoped Text Extraction  
↓  
Indicator-Specific LLM Prompt  
↓  
Structured JSON Output  
↓  
SQLite Database  
↓  
CSV Export  

---

## Generalization & Scalability

Although optimized for three known reports, the architecture is **generic by design**.

In production:
- Page hints would be replaced by TOC parsing, heading detection, or semantic search
- The same extraction loop and prompts remain unchanged
- New reports are added via configuration, not code changes

---

## Known Limitations

- Page ranges are manually configured for this exercise
- Some indicators are narrative-only or partially disclosed
- No UI or dashboard is provided

These limitations are intentional given the 3-day time constraint.

---

## Why This Approach Was Chosen

This system prioritizes:
- Accuracy over breadth
- Transparency over automation
- Shipping over perfection

It reflects how **real ESG AI systems are built incrementally**, starting with controlled, auditable pipelines before scaling.
