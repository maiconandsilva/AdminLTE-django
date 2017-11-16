// AdminLTE Gruntfile
module.exports = function (grunt) { // jshint ignore:line
    'use strict'

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        watch: {
            less: {
                // Compiles less files upon saving
                files: ['build_static/less/*.less'],
                tasks: ['less:development', 'less:production', 'replace', 'notify:less']
            },
            js: {
                // Compile js files upon saving
                files: ['build_static/js/*.js'],
                tasks: ['js', 'notify:js']
            },
            skins: {
                // Compile any skin less files upon saving
                files: ['build_static/less/skins/*.less'],
                tasks: ['less:skins', 'less:minifiedSkins', 'notify:less']
            }
        },
        // Notify end of tasks
        notify: {
            less: {
                options: {
                    title: 'AdminLTE',
                    message: 'LESS finished running'
                }
            },
            js: {
                options: {
                    title: 'AdminLTE',
                    message: 'JS bundler finished running'
                }
            }
        },
        // 'less'-task configuration
        // This task will compile all less files upon saving to create both AdminLTE.css and AdminLTE.min.css
        less: {
            // Development not compressed
            development: {
                files: {
                    // compilation.css  :  source.less
                    'static/dist/css/AdminLTE.css': 'build_static/less/AdminLTE.less',
                    // AdminLTE without plugins
                    'static/dist/css/alt/AdminLTE-without-plugins.css': 'build_static/less/AdminLTE-without-plugins.less',
                    // Separate plugins
                    'static/dist/css/alt/AdminLTE-select2.css': 'build_static/less/select2.less',
                    'static/dist/css/alt/AdminLTE-fullcalendar.css': 'build_static/less/fullcalendar.less',
                    'static/dist/css/alt/AdminLTE-bootstrap-social.css': 'build_static/less/bootstrap-social.less'
                }
            },
            // Production compressed version
            production: {
                options: {
                    compress: true
                },
                files: {
                    // compilation.css  :  source.less
                    'static/dist/css/AdminLTE.min.css': 'build_static/less/AdminLTE.less',
                    // AdminLTE without plugins
                    'static/dist/css/alt/AdminLTE-without-plugins.min.css': 'build_static/less/AdminLTE-without-plugins.less',
                    // Separate plugins
                    'static/dist/css/alt/AdminLTE-select2.min.css': 'build_static/less/select2.less',
                    'static/dist/css/alt/AdminLTE-fullcalendar.min.css': 'build_static/less/fullcalendar.less',
                    'static/dist/css/alt/AdminLTE-bootstrap-social.min.css': 'build_static/less/bootstrap-social.less'
                }
            },
            // Non minified skin files
            skins: {
                files: {
                    'static/dist/css/skins/skin-blue.css': 'build_static/less/skins/skin-blue.less',
                    'static/dist/css/skins/skin-black.css': 'build_static/less/skins/skin-black.less',
                    'static/dist/css/skins/skin-yellow.css': 'build_static/less/skins/skin-yellow.less',
                    'static/dist/css/skins/skin-green.css': 'build_static/less/skins/skin-green.less',
                    'static/dist/css/skins/skin-red.css': 'build_static/less/skins/skin-red.less',
                    'static/dist/css/skins/skin-purple.css': 'build_static/less/skins/skin-purple.less',
                    'static/dist/css/skins/skin-blue-light.css': 'build_static/less/skins/skin-blue-light.less',
                    'static/dist/css/skins/skin-black-light.css': 'build_static/less/skins/skin-black-light.less',
                    'static/dist/css/skins/skin-yellow-light.css': 'build_static/less/skins/skin-yellow-light.less',
                    'static/dist/css/skins/skin-green-light.css': 'build_static/less/skins/skin-green-light.less',
                    'static/dist/css/skins/skin-red-light.css': 'build_static/less/skins/skin-red-light.less',
                    'static/dist/css/skins/skin-purple-light.css': 'build_static/less/skins/skin-purple-light.less',
                    'static/dist/css/skins/_all-skins.css': 'build_static/less/skins/_all-skins.less'
                }
            },
            // Skins minified
            minifiedSkins: {
                options: {
                    compress: true
                },
                files: {
                    'static/dist/css/skins/skin-blue.min.css': 'build_static/less/skins/skin-blue.less',
                    'static/dist/css/skins/skin-black.min.css': 'build_static/less/skins/skin-black.less',
                    'static/dist/css/skins/skin-yellow.min.css': 'build_static/less/skins/skin-yellow.less',
                    'static/dist/css/skins/skin-green.min.css': 'build_static/less/skins/skin-green.less',
                    'static/dist/css/skins/skin-red.min.css': 'build_static/less/skins/skin-red.less',
                    'static/dist/css/skins/skin-purple.min.css': 'build_static/less/skins/skin-purple.less',
                    'static/dist/css/skins/skin-blue-light.min.css': 'build_static/less/skins/skin-blue-light.less',
                    'static/dist/css/skins/skin-black-light.min.css': 'build_static/less/skins/skin-black-light.less',
                    'static/dist/css/skins/skin-yellow-light.min.css': 'build_static/less/skins/skin-yellow-light.less',
                    'static/dist/css/skins/skin-green-light.min.css': 'build_static/less/skins/skin-green-light.less',
                    'static/dist/css/skins/skin-red-light.min.css': 'build_static/less/skins/skin-red-light.less',
                    'static/dist/css/skins/skin-purple-light.min.css': 'build_static/less/skins/skin-purple-light.less',
                    'static/dist/css/skins/_all-skins.min.css': 'build_static/less/skins/_all-skins.less'
                }
            }
        },

        // Uglify task info. Compress the js files.
        uglify: {
            options: {
                mangle: true,
                preserveComments: 'some'
            },
            production: {
                files: {
                    'static/dist/js/adminlte.min.js': ['static/dist/js/adminlte.js']
                }
            }
        },

        // Concatenate JS Files
        concat: {
            options: {
                separator: '\n\n',
                banner: '/*! AdminLTE app.js\n'
                + '* ================\n'
                + '* Main JS application file for AdminLTE v2. This file\n'
                + '* should be included in all pages. It controls some layout\n'
                + '* options and implements exclusive AdminLTE plugins.\n'
                + '*\n'
                + '* @Author  Almsaeed Studio\n'
                + '* @Support <https://www.almsaeedstudio.com>\n'
                + '* @Email   <abdullah@almsaeedstudio.com>\n'
                + '* @version <%= pkg.version %>\n'
                + '* @repository <%= pkg.repository.url %>\n'
                + '* @license MIT <http://opensource.org/licenses/MIT>\n'
                + '*/\n\n'
                + '// Make sure jQuery has been loaded\n'
                + 'if (typeof jQuery === \'undefined\') {\n'
                + 'throw new Error(\'AdminLTE requires jQuery\')\n'
                + '}\n\n'
            },
            dist: {
                src: [
                    'build_static/js/BoxRefresh.js',
                    'build_static/js/BoxWidget.js',
                    'build_static/js/ControlSidebar.js',
                    'build_static/js/DirectChat.js',
                    'build_static/js/Layout.js',
                    'build_static/js/PushMenu.js',
                    'build_static/js/TodoList.js',
                    'build_static/js/Tree.js'
                ],
                dest: 'static/dist/js/adminlte.js'
            }
        },

        // Replace image paths in AdminLTE without plugins
        replace: {
            withoutPlugins: {
                src: ['static/dist/css/alt/AdminLTE-without-plugins.css'],
                dest: 'static/dist/css/alt/AdminLTE-without-plugins.css',
                replacements: [
                    {
                        from: '../img',
                        to: '../../img'
                    }
                ]
            },
            withoutPluginsMin: {
                src: ['static/dist/css/alt/AdminLTE-without-plugins.min.css'],
                dest: 'static/dist/css/alt/AdminLTE-without-plugins.min.css',
                replacements: [
                    {
                        from: '../img',
                        to: '../../img'
                    }
                ]
            }
        },

        // Build the documentation files
        includes: {
            build: {
                src: ['*.html'], // Source files
                dest: 'documentation/', // Destination directory
                flatten: true,
                cwd: 'documentation/build',
                options: {
                    silent: true,
                    includePath: 'documentation/build_static/include'
                }
            }
        },

        // Optimize images
        image: {
            dynamic: {
                files: [
                    {
                        expand: true,
                        cwd: 'build_static/img/',
                        src: ['**/*.{png,jpg,gif,svg,jpeg}'],
                        dest: 'static/dist/img/'
                    }
                ]
            }
        },

        // Validate JS code
        jshint: {
            options: {
                jshintrc: 'build_static/js/.jshintrc'
            },
            grunt: {
                options: {
                    jshintrc: 'build_static/grunt/.jshintrc'
                },
                src: 'Gruntfile.js'
            },
            core: {
                src: 'build_static/js/*.js'
            },
            demo: {
                src: 'static/dist/js/demo.js'
            },
            pages: {
                src: 'static/dist/js/pages/*.js'
            }
        },

        jscs: {
            options: {
                config: 'build_static/js/.jscsrc'
            },
            core: {
                src: '<%= jshint.core.src %>'
            },
            pages: {
                src: '<%= jshint.pages.src %>'
            }
        },

        // Validate CSS files
        csslint: {
            options: {
                csslintrc: 'build_static/less/.csslintrc'
            },
            dist: [
                'static/dist/css/AdminLTE.css'
            ]
        },

        // Validate Bootstrap HTML
        bootlint: {
            options: {
                relaxerror: ['W005']
            },
            files: ['pages/**/*.html', '*.html']
        },

        // Delete images in build directory
        // After compressing the images in the build_static/img dir, there is no need
        // for them
        clean: {
            build: ['build_static/img/*']
        }
    })

    // Load all grunt tasks

    // LESS Compiler
    grunt.loadNpmTasks('grunt-contrib-less')
    // Watch File Changes
    grunt.loadNpmTasks('grunt-contrib-watch')
    // Compress JS Files
    grunt.loadNpmTasks('grunt-contrib-uglify')
    // Include Files Within HTML
    grunt.loadNpmTasks('grunt-includes')
    // Optimize images
    grunt.loadNpmTasks('grunt-image')
    // Validate JS code
    grunt.loadNpmTasks('grunt-contrib-jshint')
    grunt.loadNpmTasks('grunt-jscs')
    // Delete not needed files
    grunt.loadNpmTasks('grunt-contrib-clean')
    // Lint CSS
    grunt.loadNpmTasks('grunt-contrib-csslint')
    // Lint Bootstrap
    grunt.loadNpmTasks('grunt-bootlint')
    // Concatenate JS files
    grunt.loadNpmTasks('grunt-contrib-concat')
    // Notify
    grunt.loadNpmTasks('grunt-notify')
    // Replace
    grunt.loadNpmTasks('grunt-text-replace')

    // Linting task
    grunt.registerTask('lint', ['jshint', 'csslint', 'bootlint'])
    // JS task
    grunt.registerTask('js', ['concat', 'uglify'])
    // CSS Task
    grunt.registerTask('css', ['less:development', 'less:production', 'replace'])

    // The default task (running 'grunt' in console) is 'watch'
    grunt.registerTask('default', ['watch'])
}
