'use strict';

var gulp  = require('gulp');
var gutil = require('gulp-util');
var del = require('del');
var path = require('path');


var staticFiles = ['core/static/**'];
var buildDest = 'build_static/';


function clean() {
    del.sync(path.join(buildDest, '*'));
}

gulp.task('clean', function (done) {
    clean();
    done();
});


function build() {
    return (
        gulp.src(staticFiles)
        .pipe(gulp.dest(buildDest))
    );
}

gulp.task('build', ['clean'], build);


function watch() {
    gulp.watch(staticFiles, ['build']);
}

gulp.task('watch', watch);


gulp.task('default', ['build']);
