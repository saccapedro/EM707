import control as ct
import matplotlib.pyplot as plt

sys = ct.tf([1],[1, 0.5, 1])

cplt = ct.step_response(sys).plot()
plt.show()