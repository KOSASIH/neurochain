import * as THREE from 'three';
import { ARScene, ARController } from 'ar.js';

const scene = new ARScene();
const controller = new ARController(scene);

const neuroChainModel = new THREE.GLTFLoader().load('neurochain_model.gltf', (gltf) => {
    scene.add(gltf.scene);
});

controller.addEventListener('markerFound', () => {
    neuroChainModel.position.set(0, 0, -5);
    scene.add(neuroChainModel);
});

controller.addEventListener('markerLost', () => {
    scene.remove(neuroChainModel);
});
