import pandas as pd
from scipy import stats

list_freq = ['A','M','D']

di = {
    'to':['A','A','A','M','M','M','D','D','D'],
    'from':['A','M','D','A','M','D','A','M','D'],
    'value':[1,12,365,1/12,1,30,1/365,1/30,1]
}
time_converter_matrix = pd.DataFrame(di).pivot(index='from',columns='to',values='value')

def converter_factor(From:str,To:str)->float:
    """converter_factor return a conversion time factor for given time periods

    Parameters
    ----------
    from : str
        Time period to convert from
    to : str
        Time period to convert from

    Returns
    -------
    float
        conversion factor
    """
    return time_converter_matrix.loc[From,To]


def check_value_or_prob(value):

    if isinstance(value,stats._distn_infrastructure.rv_frozen):
        return value 
    else:
        value = np.atpleat_1d(value)
        assert np.issubdtype(value.dtype,np.number)
        return value
