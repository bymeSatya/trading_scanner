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

## File Structure

Trading-Scanner/
│
├── README.md
├── requirements.txt
├── main.py
├── config.py
│
├── docs/
│   ├── PROJECT_CONTEXT.md
│   ├── PROJECT_PROMPT.md
│   ├── ARCHITECTURE.md
│   ├── DECISIONS.md
│   ├── ROADMAP.md
│   ├── CODING_STANDARDS.md
│   ├── LESSONS_LEARNED.md
│   └── sprints/
│       ├── SPRINT_01.md
│       ├── SPRINT_02.md
│       └── TEMPLATE.md
│
├── data/
│   ├── loader.py
│   ├── normalizer.py
│   ├── market_store.py
│   ├── metadata_store.py          # Future
│   └── audit_logger.py            # Future
│
├── utils/
│   ├── datetime_utils.py
│   ├── file_utils.py
│   ├── spark_utils.py
│   ├── market_calendar.py         # Future
│   └── common.py
│
├── feature_engineering/
│   ├── feature_engineering.py
│   ├── candle_features.py
│   ├── trend_features.py          # Future
│   ├── volume_features.py         # Future
│   └── volatility_features.py     # Future
│
├── indicators/
│   ├── ema.py
│   ├── sma.py
│   ├── rsi.py
│   ├── macd.py
│   ├── atr.py
│   ├── vwap.py
│   └── bollinger.py
│
├── patterns/
│   ├── pattern_manager.py
│   ├── hammer.py
│   ├── doji.py
│   ├── engulfing.py
│   ├── morning_star.py
│   ├── shooting_star.py
│   ├── hanging_man.py
│   └── ...
│
├── strategies/
│   ├── strategy_manager.py
│   ├── reversal_strategy.py
│   ├── breakout_strategy.py
│   ├── pullback_strategy.py
│   └── ...
│
├── scanner/
│   ├── scanner.py
│   ├── live_scanner.py
│   ├── result_formatter.py
│   └── notifier.py                # Future
│
├── confidence/
│   ├── confidence_engine.py
│   ├── scoring_rules.py
│   └── risk_reward.py
│
├── backtesting/
│   ├── backtest_engine.py
│   ├── trade_simulator.py
│   ├── performance.py
│   └── reports.py
│
├── ml/
│   ├── dataset_builder.py
│   ├── feature_store.py
│   ├── train.py
│   ├── predict.py
│   └── models/
│
├── logs/
│   ├── application.log
│   ├── audit.log
│   └── error.log
│
├── metadata/
│   ├── latest_candle.json
│   ├── ingestion_status.json
│   └── scanner_status.json
│
├── market_data/
│   └── SYMBOL/
│       └── INTERVAL/
│           └── YEAR/
│               └── MONTH/
│                   └── YYYY_MM_DD.parquet
│
├── tests/
│   ├── test_loader.py
│   ├── test_patterns.py
│   ├── test_storage.py
│   └── test_feature_engineering.py
│
└── notebooks/
    ├── research.ipynb
    ├── strategy_testing.ipynb
    └── experiments.ipynb
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
