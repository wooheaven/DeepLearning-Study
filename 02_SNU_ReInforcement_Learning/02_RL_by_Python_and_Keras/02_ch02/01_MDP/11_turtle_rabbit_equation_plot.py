import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# ax1, ax2 : Major ticks every 10, minor ticks every 5
end_time = 40.0
ax1_major_ticks = np.arange(0, int(end_time) + 1, 10)
ax1_minor_ticks = np.arange(0, int(end_time) + 1, 5)

ax1.set_xticks(ax1_major_ticks)
ax1.set_xticks(ax1_minor_ticks, minor=True)
ax1.set_yticks(ax1_major_ticks)
ax1.set_yticks(ax1_minor_ticks, minor=True)

ax2_major_ticks = np.arange(0, int(end_time) ** 2 + 1, 10)
ax2_minor_ticks = np.arange(0, int(end_time) ** 2 + 1, 5)
ax2.set_xticks(ax2_major_ticks)
ax2.set_xticks(ax2_minor_ticks, minor=True)
ax2.set_yticks(ax2_major_ticks)
ax2.set_yticks(ax2_minor_ticks, minor=True)

# ax1, ax2 : grid
ax1.grid(which='both')
ax1.grid(which='major', alpha=0.5)
ax1.grid(which='minor', alpha=0.2)
ax2.grid(which='both')
ax2.grid(which='major', alpha=0.5)
ax2.grid(which='minor', alpha=0.2)

# ax1, ax2 : time
break_time = 10.0
ax1_turtle_time = np.arange(0.0, end_time, 0.01)
ax1_rabbit_time_1st = np.arange(0.0, break_time, 0.01)
ax1_rabbit_time_2nd = np.arange(10.0, end_time, 0.01)
ax2_turtle_time = np.arange(0.0, end_time, 0.01)
ax2_rabbit_time_1st = np.arange(0.0, break_time, 0.01)
ax2_rabbit_time_2nd = np.arange(break_time, end_time, 0.01)

# ax1, ax2 : reward
# ax1
# y = x  for  0 <= x <= end_time
# y = 2x for  0 <= x <= 10
# y = 20 for 10 <= x <= end_time
# ax2 is Integral of ax1
# y = Integral(x)dx  = x^2 / 2 for  0 <= x <= end_time
# y = Integral(2x)dx = x^2     for  0 <= x <= 10
# y = Integral(20)dx with x=10, y=100 parallel translation for 10 <= x <= end_time
ax1_turtle_reward = ax1_turtle_time
ax1_rabbit_reward_1st = 2 * ax1_rabbit_time_1st
ax1_rabbit_reward_2nd = np.ndarray(int((end_time - break_time) / 0.01))
ax1_rabbit_reward_2nd.fill(20.0)
ax2_turtle_reward = (ax2_turtle_time ** 2) / 2.0
ax2_rabbit_reward_1st = ax2_rabbit_time_1st ** 2
ax2_rabbit_reward_2nd = 20 * (ax2_rabbit_time_2nd - 10) + 100

# ax1, ax2 : line plot
ax1.plot(ax1_turtle_time, ax1_turtle_reward, 'r')
ax1.plot(ax1_rabbit_time_1st, ax1_rabbit_reward_1st, 'b')
ax1.plot(ax1_rabbit_time_2nd, ax1_rabbit_reward_2nd, 'b')
ax2.plot(ax2_turtle_time, ax2_turtle_reward, 'r')
ax2.plot(ax2_rabbit_time_1st, ax2_rabbit_reward_1st, 'b')
ax2.plot(ax2_rabbit_time_2nd, ax2_rabbit_reward_2nd, 'b')

# ax1, ax2 : graph
ax1.set_title('[Time - Reward] Plot')
ax1.set_xlabel('Time t')
ax1.set_ylabel('Reward R')
ax1.set_ylim([-5, int(end_time) + 5])
ax1.set_xlim([-5, int(end_time) + 5])
ax1.set_aspect(1)
ax1.legend(['Turtle', 'Rabbit'], loc='upper left')
ax2.set_title('[Time - Cumulative Sum of Reward] Plot')
ax2.set_xlabel('Time t')
ax2.set_ylabel('Reward R')
ax2.legend(['Turtle', 'Rabbit'], loc='upper left')

# plot
plt.show()