import * as THREE from '../node_modules/three/src/Three.js';
import WEBGL from "./WebGL.js";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
    50, 1 / 2, 0.1, 100
);

const wrapper = $("#logoWrapper");
const renderer = new THREE.WebGLRenderer({alpha: true});
renderer.setSize(wrapper.width(), wrapper.height());
wrapper.append(renderer.domElement);

const shape = new THREE.ConeGeometry(1, 2, 4);//THREE.BoxGeometry(1, 1, 0.1)
let skin = (colour) => new THREE.MeshBasicMaterial({color: colour});

const pyramid1 = new THREE.Mesh(shape, skin(0xff0683));
pyramid1.translateY(-1);
scene.add(pyramid1);

const pyramid2 = new THREE.Mesh(shape, skin(0x2233ff));
pyramid2.translateY(1);
pyramid2.rotateX(72);
scene.add(pyramid2);

camera.position.z = 6;

function animate() {
    requestAnimationFrame(animate);
    //pyramid1.rotation.x += 0.01;
    pyramid1.rotation.y += 0.01;
    //pyramid2.rotation.x += 0.01;
    pyramid2.rotation.y -= 0.01;
    renderer.render(scene, camera);
}

if (WEBGL.isWebGLAvailable()) animate();
