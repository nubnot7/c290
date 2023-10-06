from controller import Robot

bot = Robot()

timestep = 64

# Arm joints
shoulder_lift = bot.getDevice('shoulder_lift_joint')
shoulder_pan = bot.getDevice('shoulder_pan_joint')
elbow = bot.getDevice('elbow_joint')
wrist_1 = bot.getDevice('wrist_1_joint')
wrist_2 = bot.getDevice('wrist_2_joint')
wrist_3 = bot.getDevice('wrist_3_joint')

# finger 1 joints
finger_1 = bot.getDevice('palm_finger_1_joint')
finger_1_lower_knuckle = bot.getDevice('finger_1_joint_1')
finger_1_middle_knuckle = bot.getDevice('finger_1_joint_2')
finger_1_upper_knuckle = bot.getDevice('finger_1_joint_3')

# finger 2 joints
finger_2 = bot.getDevice('palm_finger_2_joint')
finger_2_lower_knuckle = bot.getDevice('finger_2_joint_1')
finger_2_middle_knuckle = bot.getDevice('finger_2_joint_2')
finger_2_upper_knuckle = bot.getDevice('finger_2_joint_3')

# finger middle joints
finger_3_lower_knuckle = bot.getDevice('finger_middle_joint_1')
finger_3_middle_knuckle = bot.getDevice('finger_middle_joint_2')
finger_3_upper_knuckle = bot.getDevice('finger_middle_joint_3')

# get the distance sensor node
sensor = bot.getDevice('distance sensor')

# enabling the distance sensor
sensor.enable(timestep)



# method to move the arm
def move_bot(a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, 
             g = 0.17, h = 0.05, i = 0, j = -0.06):
    
    joint_limits = {
        shoulder_lift: (-2.0, 2.0),
        shoulder_pan: (-3.14, 3.14),
    }
    
    for joint, (min_limit, max_limit) in joint_limits.items():
        a = max(min_limit, min(a, max_limit))
    # arm joints
    shoulder_lift.setPosition(a)
    shoulder_pan.setPosition(b)
    elbow.setPosition(c)
    wrist_1.setPosition(d)
    wrist_2.setPosition(e)
    wrist_3.setPosition(f)
    
    # finger palm joints
    finger_1.setPosition(g)
    finger_2.setPosition(g)
    
    # finger lower knuckle motor
    finger_1_lower_knuckle.setPosition(h)
    finger_2_lower_knuckle.setPosition(h)
    finger_3_lower_knuckle.setPosition(h)
    
    # finger middle knuckle motor
    finger_1_middle_knuckle.setPosition(i)
    finger_2_middle_knuckle.setPosition(i)
    finger_3_middle_knuckle.setPosition(i)
    
    # finger upper knuckle motor
    finger_1_upper_knuckle.setPosition(j)
    finger_2_upper_knuckle.setPosition(j)
    finger_3_upper_knuckle.setPosition(j)
    

# moving bot at initial positions
move_bot()


#  method to add delay
def add_delay(delay_time_steps):

    time_counter = 0
    while bot.step(timestep)  !=  -1:
        if time_counter  >=  delay_time_steps:
            break
        
        time_counter += 1



while bot.step(timestep)  !=  -1:

    # get the value from the sensor
    val = sensor.getValue()
    if val < 400:
        
        move_bot(0.15, 1.57, -0.1, -0.04, h = 0.3, i = 0.3)
        add_delay(10) 
        
        move_bot(-0.1, 1.57, 0, 0, h = 0.3, i = 0.3)
        add_delay(10)
        
        move_bot(-0.1, -0.01, 0, 0, h = 0.3, i = 0.3)
        add_delay(10)   
        
        move_bot(-0.1, -0.01, 0, 0, h = 0.05, i = 0)
        add_delay(10)
        
        move_bot(-0.1, 1.57)
        add_delay(10)
    
    else:
        move_bot(0.15, 1,57, -0.1, -0.04)
    
    # print the distance
    print('Distance : ', val)
    
    #  move the arom over conveyor
 
