openssl aes-256-cbc -K $encrypted_db2095f63ba3_key -iv $encrypted_db2095f63ba3_iv -in .travis/deploy_rsa.enc -out .travis/deploy_rsa -d
eval "$(ssh-agent -s)"
cp .travis/deploy_rsa ~/.ssh/deploy_rsa
chmod 600 ~/.ssh/deploy_rsa
ssh-add ~/.ssh/deploy_rsa