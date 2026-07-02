# Design Decisions

Decision 001

Store one trading day per Parquet.

Reason

Easy incremental updates.

Easy debugging.

Fast reads.

---

Decision 002

Store Trade_Date separately.

Reason

Required by storage.

Backtesting.

ML.

Metadata.

---

Decision 003

Convert UTC to IST before storage.

Reason

Business timezone.

Avoid repeated conversion.

---

Decision 004

One pattern = one file.

Reason

Easy maintenance.

Easy testing.

Easy extension.

---

Decision 005

Spark after ingestion.

Reason

Yahoo returns Pandas.

Everything else uses Spark.