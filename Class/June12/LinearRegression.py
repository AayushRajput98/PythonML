import numpy as np
from matplotlib import pyplot as plt
def estimate_coef(x,y):
    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    SS_xy = np.sum(y*x - n*m_y*m_x)
    SS_xx = np.sum(x*x - n*m_x*m_x)
    b_1 = SS_xy/SS_xx
    b_0 = m_y - b_1*m_x
    return  b_0, b_1
def plot_regression_line(x,y,b):
    plt.scatter(x, y, color = 'm', marker= 'o', s=30)
    y_pred = b[0]+b[1]*x
    plt.plot(x, y_pred, color='g')
    plt.title('Linear Regression')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
x=np.arange(10)
y=np.array([1,3,2,5,7,4,9,7,4,9])
b = estimate_coef(x,y)
plot_regression_line(x,y,b)