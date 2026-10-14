import xml.etree.ElementTree as ET


def parse_xml(file_path):

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        name = root.get('name')
        print(f"Fetched {name} ")

        joint_count = 0
        link_count = 0

        joint_names = []
        link_names = []

        joint_grabber = root.findall('joint')
        for joint in joint_grabber:
            joint_count += 1
            joint_names.append(joint.get('name'))

        link_grabber = root.findall('link')
        for link in link_grabber:
            link_count += 1
            link_names.append(link.get('name'))

        print(
            f"There are {joint_count} joints and {link_count} links in {name}")
        if joint_count == 6 or joint_count == 7:

            print("lots of degrees....good luck bub")
        elif joint_count > 6:
            print("Its a robot with more than 6 DOF....why do this to yourself....?")
        return root, joint_names, link_names
    except:
        print(f"Error parsing XML file: {file_path}")
        return None


# Set to Puma 560 for now, but use this to call the function, but make sure the urdf file is accessible...bad things happened last ime
puma_root, puma_joint_names, puma_link_names = parse_xml(
    "C:/StarterTemplates/Webots/PUMA560/Modified_URDF/PUMA560Robot.urdf")

robot_dict = {
    "root": puma_root,
    "joint_names": puma_joint_names,
    "link_names": puma_link_names

}
