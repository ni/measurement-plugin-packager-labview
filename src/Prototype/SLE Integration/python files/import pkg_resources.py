import pkg_resources

def get_package_location(package_name):
    distribution = pkg_resources.get_distribution(package_name)
    return distribution.location

if __name__ == "__main__":
    import sys
    package_name = sys.argv[1]
    print(get_package_location(package_name))
