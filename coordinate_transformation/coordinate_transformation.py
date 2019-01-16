import numpy as np

def polar_coordinate_conversion(x,y,z,normalization=None):
    '''
    球座標系への変換
    x，y，z:np.array形式
    normalization:正規化するかどうか
    '''
    r=np.sqrt(x**2+y**2+z**2)
    if normalization =='r_zscore':
        r = (r-np.mean(r,axis=0))/np.std(r,axis=0)
    phi = np.arctan2(y,x)
    theta = np.arctan2(np.sqrt(x**2+y**2),z)
    return (r,phi,theta)


def resolve_polar_coordinate_conversion(r,phi,theta):
    '''
    デカルト座標系への復元
    ただし、zscoreは戻せないので注意
    r,phi,theta:np.array形式
    '''
    x_ = r*np.sin(theta)*np.cos(phi)
    y_ = r*np.sin(theta)*np.sin(phi)
    z_ = r*np.cos(theta)
    return(x_,y_,z_)