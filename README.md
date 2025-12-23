# ROS 2 Obstacle Avoidance Robot 🤖🚀

Ce projet implémente un système d'évitement d'obstacles autonome pour un robot **TurtleBot3 (Burger)** utilisant **ROS 2 Humble** et le simulateur **Gazebo**.

## 📋 Description
Le robot utilise un capteur **Lidar** pour scanner son environnement en temps réel. Un script Python traite les données laser et commande les moteurs du robot pour éviter les collisions avec les murs et les obstacles dans un environnement 3D.

## 🛠️ Technologies utilisées
*   **OS:** Ubuntu 22.04 (Jammy Jellyfish)
*   **Middleware:** ROS 2 Humble
*   **Simulateur:** Gazebo
*   **Langage:** Python 3
*   **Robot:** TurtleBot3 Burger

## 🚀 Installation

1.  **Prérequis :** Avoir ROS 2 Humble et les paquets TurtleBot3 installés.
2.  
3.  **Cloner le dépôt :**
    ```bash
    cd ~/ros2_ws/src
    git clone https://github.com/AfrahSalem/ROS2-Obstacle-Avoidance.git
    ```
4.  **Compiler le projet :**
    ```bash
    cd ~/ros2_ws
    colcon build --packages-select robot_evader
    source install/setup.bash
    ```

## 🎮 Utilisation

1.  **Lancer la simulation Gazebo :**
    ```bash
    export TURTLEBOT3_MODEL=burger
    ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
    ```

2.  **Lancer le nœud d'évitement d'obstacles :**
    ```bash
    ros2 run robot_evader avoid_walls
    ```

## 📺 Démonstration
(https://www.linkedin.com/feed/update/urn:li:activity:7409001493883899904/)
