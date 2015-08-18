'use strict';

var gulp  = require('gulp');
var gutil = require('gulp-util');
var del = require('del');
var path = require('path');
var bower = require('gulp-bower');


var staticFiles = ['core/static/**'];
var buildDest = 'build_static/';


function clean() {
    del.sync(path.join(buildDest, '*'));
}

gulp.task('clean', clean);


function copyBowerPackage(name, files) {
    gulp.src(path.join('bower_components/', name, files))
        .pipe(gulp.dest(path.join(buildDest, path.join('dist/', name))));
}

function build() {
    gulp.src(staticFiles)
        .pipe(gulp.dest(buildDest));

    bower();

    copyBowerPackage('bootstrap', 'dist/**');
    copyBowerPackage('jquery', 'dist/**');
    copyBowerPackage('js-cookie', 'src/**');
    copyBowerPackage('underscore', '*');
}

gulp.task('build', ['clean'], build);


function watch() {
    gulp.watch(staticFiles, ['build']);
}

gulp.task('watch', watch);


gulp.task('default', ['build']);
