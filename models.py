"""
AI-Powered Student Grade Tracker - Database Models
==================================================
Comprehensive SQLAlchemy ORM models for academic performance management system
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
from sqlalchemy.orm import relationship
from sqlalchemy import func, text
import json

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """
    Base user model supporting multiple roles (student, teacher, admin, parent)
    """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student')  # student, teacher, admin, parent
