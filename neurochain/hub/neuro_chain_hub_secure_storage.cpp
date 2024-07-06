#include <seal/seal.h>
#include <neuro_chain_hub/neuro_chain_hub.h>

int main() {
    seal::SEALContext context(seal::SEALContext::Create());
    seal::KeyGenerator keygen(context);
    seal::PublicKey public_key = keygen.public_key();
    seal::SecretKey secret_key = keygen.secret_key();
    NeuroChainHub hub;
    hub.init(public_key, secret_key);
    // encrypt and store data
    seal::Ciphertext encrypted_data;
    hub.encrypt_data("Hello, World!", encrypted_data);
    // store encrypted data
    hub.store_data(encrypted_data);
    return 0;
}
