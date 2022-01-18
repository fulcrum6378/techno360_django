import * as THREE from '../node_modules/three/src/Three.js';
import WEBGL from "./WebGL.js";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
    75, window.innerWidth / window.innerHeight, 0.1, 1000
);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth / 2, window.innerHeight / 2);
$("#intro").append(renderer.domElement);

const cube = new THREE.Mesh(
    new THREE.BoxGeometry(),
    new THREE.MeshBasicMaterial({color: 0x00ff00})
);
scene.add(cube);
camera.position.z = 5;

function animate() {
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    renderer.render(scene, camera);
}

if (WEBGL.isWebGLAvailable()) animate();
