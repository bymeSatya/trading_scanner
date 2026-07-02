# Trading Scanner Project Context

## Project Goal

Build a production-ready intraday stock scanner using PySpark.

This project is being built from scratch for learning Data Engineering, PySpark, Software Architecture and Quantitative Trading.

The application is intended for personal use and future ML research.

---

## Objectives

- Learn PySpark professionally
- Build production-quality ETL pipelines
- Build reusable feature engineering modules
- Detect candlestick patterns
- Build strategy engine
- Build confidence scoring engine
- Backtesting
- ML Feature Store
- Future AI Assistant

---

## Current Architecture

Yahoo Finance
↓

Loader

↓

Normalizer

↓

Datetime Utils

↓

Spark DataFrame

↓

Market Store

↓

Feature Engineering

↓

Pattern Detection

↓

Strategy Manager

↓

Scanner

↓

Backtesting

↓

Machine Learning

---

## Storage Design

market_data/

    SYMBOL/

        INTERVAL/

            YEAR/

                MONTH/

                    YYYY_MM_DD.parquet

Example

market_data/

    RELIANCE/

        5m/

            2026/

                06/

                    2026_06_29.parquet

---

## Data Schema

Symbol

Datetime (IST)

Trade_Date

Open

High

Low

Close

Volume

---

## Design Principles

- Convert UTC to IST before storage.
- Trade_Date is stored as a separate column.
- Spark is used after ingestion.
- Daily Parquet files.
- One responsibility per module.
- Configuration driven.
- Production-first architecture.
- Simplicity over premature optimization.

---

## Completed

✓ Loader

✓ Normalizer

✓ UTC → IST conversion

✓ Trade_Date

✓ Hammer Pattern

✓ Pattern Manager

---

## Current Sprint

Sprint 2

Market Storage Engine

Current Task

Implement save_market_data()

---

## Future Modules

Metadata Manager

Audit Logger

Feature Engineering

Indicators

Pattern Detection

Strategy Manager

Confidence Engine

Scanner

Backtesting

ML Feature Store

AI Models