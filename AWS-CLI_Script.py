#Create a Vault in AWS Glacier
aws glacier create-vault --vault-name TestVault --acount-id -

#Upload Archives to a Vault
aws glacier upload-archive --acount-id - --vault-name TestVault --body File1.txt

aws glacier upload-archive --acount-id - --vault-name TestVault --body File2.txt

#Initiate Job to retrieve Archieve inventory of a Vault
aws glacier initiate-job --account-id - --valut-name TestVault --job-parameter file://inventory-retrieval.json

#Initiate Job to retrieve an uploaded file
aws glacier initiate-job --account-id - --valut-name TestVault --job-parameter file://job-archive-retrieval.json

#Describe an Active Job
aws glacier describe-job --account-id - --vault-name TestVault --job-id <<job-id>>

#List All active Jobs
aws glacier list-jobs --account-id - --vault-name TestVault

#Describe a Vault
aws glacier describe-vault --vault-name TestVault --account-id -

#Get Job Output
aws glacier get-job-output --account-id - --vault-name TestVault --job-id <<job-id>>
