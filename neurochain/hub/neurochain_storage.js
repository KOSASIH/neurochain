import { NeuroChainStorage } from 'neurochain-hub-storage';

const storage = new NeuroChainStorage();

async function storeData(data) {
    try {
        await storage.put(data);
        console.log("Data stored successfully!");
    } catch (error) {
        console.error("Error storing data:", error);
    }
}

storeData({ foo: 'bar' });
