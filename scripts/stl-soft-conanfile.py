from conans import ConanFile

class STLSoftConan(ConanFile):
    name = "stl-soft"
    version = "1.9.119"
    # No settings/options are necessary, this is header only
    export_source = "include/*"
    no_copy_source = False

    def package(self):
        self.copy("*")
