__version_info__ = {
    'major': 0,
    'minor': 2,
    'micro': 2,
    'releaselevel': 'beta',
    'serial': 1
}


def get_version(short=False):
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i.%(micro)i" % __version_info__]
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('%s%i' % (__version_info__['releaselevel'][0],
                              __version_info__['serial']))
    return ''.join(vers)

__version__ = get_version()