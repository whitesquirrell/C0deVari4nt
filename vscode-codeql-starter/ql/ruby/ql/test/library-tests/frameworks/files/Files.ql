private import ruby
private import codeql.ruby.frameworks.Files
private import codeql.ruby.Concepts

query predicate fileInstances(File::FileInstance i) { any() }

query predicate ioInstances(IO::IOInstance i) { any() }

query predicate fileReaders(File::FileModuleReader r) { any() }

query predicate ioReaders(IO::IOReader r, string api) { api = r.getAPI() }

query predicate ioFileReaders(IO::IOFileReader r, string api) { api = r.getAPI() }

query predicate fileModuleFilenameSources(File::FileModuleFilenameSource s) { any() }

query predicate fileUtilsFilenameSources(FileUtils::FileUtilsFilenameSource s) { any() }

query predicate fileSystemReadAccesses(FileSystemReadAccess a) { any() }

query predicate fileNameSources(FileNameSource s) { any() }
