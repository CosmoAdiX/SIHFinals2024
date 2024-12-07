import iphone from '../src/assets/3DModels/iphone_x_lowpoly/scene.gltf';
import React, { useRef, useEffect } from 'react';
import { useGLTF, useScroll } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';

export function Iphone(props) {
  const { nodes, materials } = useGLTF(iphone);
  const phoneRef = useRef();
  const scroll = useScroll();

  // Use frame to animate on scroll
  useFrame(() => {    
    // Animate position based on scroll
    phoneRef.current.position.y = -4 + scroll.offset * 10; // Adjusts height based on scroll
    // Rotate the phone as it moves
    phoneRef.current.rotation.y = Math.min(scroll.offset * 10, 5) // Adjust rotation speed as needed
  });

  return (
    <group castShadow receiveShadow ref={phoneRef} position={[0,0,0]} {...props} dispose={null}>
      <group rotation={[0, 0, 1.8]}>
        <group>
          <mesh geometry={nodes['phone_01_-_Default_0'].geometry} material={materials['01_-_Default']} />
          <mesh geometry={nodes['phone_03_-_Default_0'].geometry} material={materials['03_-_Default']} />
          <mesh geometry={nodes['phone_10_-_Default_0'].geometry} material={materials['10_-_Default']} />
          <mesh geometry={nodes['phone_02_-_Default_0'].geometry} material={materials['02_-_Default']} />
          <mesh geometry={nodes.phone_wbite_0.geometry} material={materials.wbite} />
          <mesh geometry={nodes.phone_lightmetal_0.geometry} material={materials.lightmetal} />
          <mesh geometry={nodes['phone_13_-_Default_0'].geometry} material={materials['13_-_Default']} />
        </group>
      </group>
      {/* Additional groups and meshes remain unchanged */}
      {/* ... */}
    </group>
  );
}

useGLTF.preload(iphone);