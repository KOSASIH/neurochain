#include <iostream>
#include <string>
#include "neurochain_qr_crypto.h"

int main() {
    NeuroChainQRCrypto crypto;
    std::string message = "Hello, NeuroChain!";
    std::string encrypted_message = crypto.encrypt(message);
    std::string decrypted_message = crypto.decrypt(encrypted_message);
    std::cout << "Encrypted message: " << encrypted_message << std::endl;
    std::cout << "Decrypted message: " << decrypted_message << std::endl;
    return 0;
}
