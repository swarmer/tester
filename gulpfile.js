'use strict';

var gulp  = require('gulp');
var gutil = require('gulp-util');
var del = require('del');
var path = require('path');
var bower = require('gulp-bower');
var autoprefixer = require('autoprefixer-core');
var cssnano = require('cssnano');
var postcss = require('gulp-postcss');
var rename = require('gulp-rename');
var sourcemaps = require('gulp-sourcemaps');


var staticFiles = ['core/static/**'];
var buildDest = 'build_static/';

function copyBowerPackage(name, files) {
    gulp.src(path.join('bower_components/', name, files))
        .pipe(gulp.dest(path.join(buildDest, path.join('dist/', name))));
}

gulp.task('clean', function () {
    del.sync(path.join(buildDest, '*'));
});

gulp.task('copyStatic', ['clean'], function () {
    return gulp.src(staticFiles)
        .pipe(gulp.dest(buildDest));
});

gulp.task('css', ['copyStatic'], function () {
    var processors = [
        autoprefixer({
            browsers: 'last 2 versions'
        }),
        cssnano({
            autoprefixer: false,
            merge: false,
            idents: false,
            unused: false,
            zindex: false
        })
    ];
    return gulp.src('build_static/*/*.css')
        .pipe(sourcemaps.init({loadMaps: true}))
            .pipe(postcss(processors))
            .pipe(rename({extname: '.min.css'}))
        .pipe(sourcemaps.write('.', {sourceRoot: '/static/'}))
        .pipe(gulp.dest('build_static/'));
});

gulp.task('bower', ['clean'], function () {
    bower();
    copyBowerPackage('bootstrap', 'dist/**');
    copyBowerPackage('jquery', 'dist/**');
    copyBowerPackage('js-cookie', 'src/**');
    copyBowerPackage('underscore', '*');
});

gulp.task('build', ['copyStatic', 'css', 'bower']);

gulp.task('watch', function () {
    gulp.watch([staticFiles, 'bower.json'], ['build']);
});

gulp.task('default', ['build']);
