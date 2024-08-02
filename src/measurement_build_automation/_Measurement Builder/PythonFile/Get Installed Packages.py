import pkg_resources

def get_package_location(package_name):
    distribution = pkg_resources.get_distribution(package_name)
    return distribution.location
