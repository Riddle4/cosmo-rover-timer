# Cosmo Rover

Premiere version simple du projet `cosmo_rover` pour valider le workflow :

Mac -> GitHub -> Ubuntu avec ROS 2 Lyrical et Gazebo.

Cette version contient uniquement :

- un package Python ROS 2 nomme `cosmo_rover`
- un node timer qui affiche le temps ecoule toutes les secondes
- un launch file pour demarrer le node
- un monde Gazebo simple avec un sol plat, une piste rectangulaire et une ligne de depart

Il n'y a pas encore de robot complexe ni de controleur de vitesse.

## Structure

```text
ros2_ws/
  src/
    cosmo_rover/
      cosmo_rover/
        timer_node.py
      launch/
        rover_timer.launch.py
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

Depuis le dossier `ros2_ws` :

```bash
gz sim src/cosmo_rover/worlds/simple_track.sdf
```

Le monde contient un sol plat, une piste rectangulaire simple et une ligne de depart visible.
