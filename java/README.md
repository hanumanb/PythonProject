# Java implementation

Requires Java 17+ and Maven 3.8+.

Run from this directory:

```bash
mvn clean package
mvn exec:java -Dexec.args="../../sample-data/application.log"
```

The Java version demonstrates parsing, grouping, severity classification, recommendations,
and CSV export. It uses only the JDK, so no external runtime dependencies are needed.
