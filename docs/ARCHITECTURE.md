# Architecture

Every module has one responsibility.

Loader
↓

Downloads data.

Normalizer
↓

Converts Yahoo format into standard schema.

Datetime Utils
↓

Timezone conversion.

Trade_Date generation.

Market Store
↓

Stores historical market data.

Feature Engineering
↓

Creates reusable columns.

Pattern Detection
↓

Detects candlestick patterns.

Strategy Manager
↓

Combines multiple patterns.

Scanner
↓

Produces trading opportunities.

Backtesting
↓

Validates strategies.

Machine Learning
↓

Uses stored historical data.