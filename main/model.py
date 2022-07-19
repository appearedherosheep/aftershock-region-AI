import pandas as pd

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

from shapely.geometry import Point
from shapely.affinity import scale, rotate

def PolyLR():
    path = 'D:/github/aftershock-region-AI/data/aftershock-region.csv'
    data = pd.read_csv(path)
    data = data.dropna()
    x = data[['magnitude']]
    y = data[['region']]

    model = make_pipeline(PolynomialFeatures(
        degree=8, include_bias=True), LinearRegression())
    score = cross_val_score(model, x, y, scoring='r2',
                            cv=KFold(n_splits=5, shuffle=True),)

    X_train, X_test, y_train, y_test = train_test_split(x, y, shuffle=True)

    model = make_pipeline(PolynomialFeatures(
        degree=8, include_bias=True), LinearRegression())
    model.fit(X_train, y_train)
    return model

def LongMinorAxis(s):
    pi = 3.1415926535897932384626433832795028841971
    return (s/0.6*pi)**(1/2), (0.6*s/pi)**(1/2)

def cvt2degree(a, b):
    k = 1/(1.68*60)
    return a*k, b*k

def returnEllipse(center, theta, Long, Minor):
    long, minor = cvt2degree(Long, Minor)
    e = 0.8
    s = Point(center)
    r = long
    alpha = theta
    circle = s.buffer(r)
    ellipse = scale(circle, 1, (1-e*e)**(1/2))
    ellipse = rotate(ellipse, alpha, use_radians=True)
    # print(ellipse.exterior.coords)
    return ellipse