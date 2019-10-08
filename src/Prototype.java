// Imports the Google Cloud client library
import com.google.cloud.bigquery.BigQuery;
import com.google.cloud.bigquery.BigQueryOptions;
import com.google.cloud.bigquery.Dataset;
import com.google.cloud.bigquery.DatasetInfo;

import com.google.cloud.storage.Bucket;
import com.google.cloud.storage.BucketInfo;
import com.google.cloud.storage.Storage;
import com.google.cloud.storage.StorageOptions;

public class Prototype {

    // Replace this with your PATH. Not sure how to do relative path in Java
    private String GOOGLE_APPLICATION_CREDENTIALS= "/Users/abigail_tran/Documents/SeniorProject/GoogleAPI/GoogleAPI/proven-now.json";
    private GOOGLE_CLOUD_PROJECT="proven-now-254616";

//    public static void main(String... args) throws Exception {
//        // Instantiate a client. If you don't specify credentials when constructing a client, the
//        // client library will look for credentials in the environment, such as the
//        // GOOGLE_APPLICATION_CREDENTIALS environment variable.
//        BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();
//
//        // The name for the new dataset
//        String datasetName = "my_new_dataset";
//
//        // Prepares a new dataset
//        Dataset dataset = null;
//        DatasetInfo datasetInfo = DatasetInfo.newBuilder(datasetName).build();
//
//        // Creates the dataset
//        dataset = bigquery.create(datasetInfo);
//
//        System.out.printf("Dataset %s created.%n", dataset.getDatasetId().getDataset());
//    }


    public static void main(String... args) throws Exception {
        // Instantiates a client
        Storage storage = StorageOptions.getDefaultInstance().getService();

        // The name for the new bucket
        String bucketName = args[0];  // "my-new-bucket";

        // Creates the new bucket
        Bucket bucket = storage.create(BucketInfo.of(bucketName));

        System.out.printf("Bucket %s created.%n", bucket.getName());
    }


    static void authImplicit() {
        // If you don't specify credentials when constructing the client, the client library will
        // look for credentials via the environment variable GOOGLE_APPLICATION_CREDENTIALS.
        Storage storage = StorageOptions.getDefaultInstance().getService();

        // You can specify a credential file by providing a path to GoogleCredentials.
        // Otherwise credentials are read from the GOOGLE_APPLICATION_CREDENTIALS environment variable.
//        GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream(jsonPath))
//                .createScoped(Lists.newArrayList("https://www.googleapis.com/auth/cloud-platform"));



        System.out.println("Buckets:");
        Page<Bucket> buckets = storage.list();
        for (Bucket bucket : buckets.iterateAll()) {
            System.out.println(bucket.toString());
        }
    }
}
