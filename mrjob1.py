from mrjob.job import MRJob
class CreditCardFraudDetectionMRJob(MRJob):

    def mapper(self, _, line):
        # Split the CSV line into fields
        fields = line.strip().split(',')

        # Assuming the first column is the transaction ID and the last column is the transaction class
        transaction_id = fields[0]
        transaction_class = int(fields[-1])

        # Emit key-value pairs with transaction ID as the key and transaction class as the value
        yield transaction_id, transaction_class

    def reducer(self, transaction_id, classes):
        # Count the number of transactions for each class
        num_normal_transactions = 0
        num_fraudulent_transactions = 0

        for transaction_class in classes:
            if transaction_class == 0:
                num_normal_transactions += 1
            else:
                num_fraudulent_transactions += 1

        # Output the transaction ID and the counts of normal and fraudulent transactions
        yield transaction_id, (num_normal_transactions, num_fraudulent_transactions)

if __name__ == '__main__':
    CreditCardFraudDetectionMRJob.run()
