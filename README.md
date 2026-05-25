# Cosmo Rover

Premiere version simple du projet `cosmo_rover` pour valider le workflow :

Mac -> GitHub -> Ubuntu avec ROS 2 Lyrical et Gazebo.

Cette version contient uniquement :

- un package Python ROS 2 nomme `cosmo_rover`
- un node timer qui affiche le temps ecoule toutes les secondes
- un launch file pour demarrer le node
- un monde Gazebo simple avec un sol plat, une piste rectangulaire et une ligne de depart
- un modele Gazebo simple de rover a 4 roues
- un node ROS 2 simple de teleoperation clavier qui publie sur `/cmd_vel`

Il n'y a pas encore de robot complexe ni de controleur de vitesse avance.

## Structure

```text
ros2_ws/
  src/
    cosmo_rover/
      cosmo_rover/
        drive_node.py
        timer_node.py
      launch/
        drive_rover.launch.py
        rover_timer.launch.py
      models/
        cosmo_rover/
          model.config
          model.sdf
      worlds/
        simple_track.sdf
      package.xml
      setup.py
      setup.cfg
```

## Construire sur Ubuntu

Depuis la racine du depot :

```bash
cd ros2_ws
source /opt/ros/lyrical/setup.bash
colcon build
source install/setup.bash
```

Si `source /opt/ros/lyrical/setup.bash` est deja dans ton `.bashrc`, tu n'as pas besoin de le refaire dans chaque terminal.

Le launch de conduite utilise `ros_gz_bridge`. Si le package manque sur Ubuntu :

```bash
sudo apt install ros-lyrical-ros-gz-bridge
```

## Lancer le node timer

```bash
ros2 launch cosmo_rover rover_timer.launch.py
```

Le terminal doit afficher :

```text
Cosmo Rover Timer started
Elapsed time: 1 seconds
Elapsed time: 2 seconds
Elapsed time: 3 seconds
```

## Lancer le monde Gazebo

Option recommandee, via ROS 2 launch. Cette commande lance Gazebo et le bridge `/cmd_vel` :

```bash
ros2 launch cosmo_rover drive_rover.launch.py
```

Dans un deuxieme terminal, lance le controle clavier :

```bash
cd ~/CosmoRobotics/cosmo-rover-timer/ros2_ws
source /opt/ros/lyrical/setup.bash
source install/setup.bash
ros2 run cosmo_rover drive_node
```

Option directe, depuis le dossier `ros2_ws` :

```bash
GZ_SIM_RESOURCE_PATH=$PWD/src/cosmo_rover/models gz sim -r src/cosmo_rover/worlds/simple_track.sdf
```

Le monde contient un sol plat, une piste rectangulaire simple, une ligne de depart visible et le rover place pres de cette ligne.

Le modele du rover est dans :

```text
src/cosmo_rover/models/cosmo_rover/model.sdf
```

Le node de conduite lit les touches du clavier et publie sur `/cmd_vel`.

Commandes clavier :

```text
fleche haut    : avancer
fleche bas     : reculer
fleche gauche  : tourner a gauche
fleche droite  : tourner a droite
q              : augmenter la vitesse
a              : diminuer la vitesse
espace         : stopper
Ctrl+C         : quitter
```

## Commander manuellement le rover

Si Gazebo et le bridge sont deja lances, tu peux aussi publier une commande ROS 2 a la main :

```bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.25}, angular: {z: 0.0}}" --rate 10
```

Pour une commande manuelle avec Gazebo lance directement, demarre aussi le bridge dans un autre terminal :

```bash
ros2 run ros_gz_bridge parameter_bridge /cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist
```
