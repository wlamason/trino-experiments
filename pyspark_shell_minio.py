"""The below script is assumed to be run in a pyspark shell."""

"""
# Not needed, but one way to configure s3 access.
export AWS_ACCESS_KEY=minio
# Not needed, but one way to configure s3 access.
export AWS_SECRET_KEY=minio123

# Run this command.
pyspark \
--jars hadoop-aws-3.3.4.jar,aws-java-sdk-bundle-1.12.576.jar \
--conf spark.hadoop.fs.s3a.endpoint=http://localhost:9000 \
--conf spark.hadoop.fs.s3a.access.key=minio \
--conf spark.hadoop.fs.s3a.secret.key=minio123 \
--conf spark.hadoop.fs.s3a.path.style.access=true \
--conf spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem
"""

spark.sparkContext.getConf().getAll()
"""
[
    ("spark.hadoop.fs.s3a.access.key", "minio"),
    ("spark.hadoop.fs.s3a.path.style.access", "true"),
    (
        "spark.repl.local.jars",
        "file:///home/wlamason/src/trino-experiments/hadoop-aws-3.3.4.jar,file:///home/wlamason/src/trino-experiments/aws-java-sdk-bundle-1.12.576.jar",
    ),
    ("spark.app.startTime", "1698802146513"),
    (
        "spark.jars",
        "file:///home/wlamason/src/trino-experiments/hadoop-aws-3.3.4.jar,file:///home/wlamason/src/trino-experiments/aws-java-sdk-bundle-1.12.576.jar",
    ),
    ("spark.executor.id", "driver"),
    ("spark.hadoop.fs.s3a.endpoint", "http://localhost:9000"),
    ("spark.app.name", "PySparkShell"),
    ("spark.driver.host", "172.25.127.228"),
    (
        "spark.driver.extraJavaOptions",
        "-Djava.net.preferIPv6Addresses=false -XX:+IgnoreUnrecognizedVMOptions --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.lang.invoke=ALL-UNNAMED --add-opens=java.base/java.lang.reflect=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.util.concurrent=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/sun.nio.cs=ALL-UNNAMED --add-opens=java.base/sun.security.action=ALL-UNNAMED --add-opens=java.base/sun.util.calendar=ALL-UNNAMED --add-opens=java.security.jgss/sun.security.krb5=ALL-UNNAMED -Djdk.reflect.useDirectMethodHandle=false",
    ),
    ("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem"),
    ("spark.app.id", "local-1698802147035"),
    ("spark.sql.catalogImplementation", "hive"),
    ("spark.app.submitTime", "1698802146272"),
    ("spark.rdd.compress", "True"),
    (
        "spark.app.initial.jar.urls",
        "spark://172.25.127.228:41705/jars/aws-java-sdk-bundle-1.12.576.jar,spark://172.25.127.228:41705/jars/hadoop-aws-3.3.4.jar",
    ),
    ("spark.serializer.objectStreamReset", "100"),
    ("spark.master", "local[*]"),
    ("spark.submit.pyFiles", ""),
    ("spark.submit.deployMode", "client"),
    ("spark.hadoop.fs.s3a.secret.key", "minio123"),
    ("spark.driver.port", "41705"),
    ("spark.ui.showConsoleProgress", "true"),
    (
        "spark.executor.extraJavaOptions",
        "-Djava.net.preferIPv6Addresses=false -XX:+IgnoreUnrecognizedVMOptions --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.lang.invoke=ALL-UNNAMED --add-opens=java.base/java.lang.reflect=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.util.concurrent=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/sun.nio.cs=ALL-UNNAMED --add-opens=java.base/sun.security.action=ALL-UNNAMED --add-opens=java.base/sun.util.calendar=ALL-UNNAMED --add-opens=java.security.jgss/sun.security.krb5=ALL-UNNAMED -Djdk.reflect.useDirectMethodHandle=false",
    ),
]
"""

df = spark.createDataFrame(
    [
        {"age": 1, "name": "a"},
        {"age": 1, "name": "b"},
        {"age": 1, "name": "c"},
        {"age": 1, "name": "d"},
        {"age": 1, "name": "e"},
        {"age": 1, "name": "f"},
        {"age": 1, "name": "g"},
    ]
)


df.show()


df.write.json("s3a://datalake/test", mode="overwrite")
