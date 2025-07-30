// app/configs/middlewares.js
import dotenv from 'dotenv';

dotenv.config();

export const notFoundHandler = (req, res, next) => {
  if (req.method === 'GET') {
    return res.status(404).render('not-found', {
      url: req.originalUrl,
      title: 'Página no encontrada'
    });
  }

  res.status(404).json({
    error: 'Not Found',
    path: req.originalUrl,
    method: req.method
  });
};

export const redirectIfLoggedIn = (req, res, next) => {
  if (req.session.user) {
    return res.redirect('/');
  }
  next();
};

export const requireLogin = (req, res, next) => {
  if (!req.session || !req.session.user) {
    req.flash('error', 'Debes iniciar sesión para continuar');
    return res.redirect('/sign-in');
  }
  next();
};


export const loadEnv = (req, res, next) => {
  res.locals = {
    ...res.locals,
    env: process.env,
    title: process.env.APP_NAME
  };
  next();
};

export const errorHandler = (err, req, res, next) => {
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  res.status(err.status || 500);
  res.render('session/error');
};