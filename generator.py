#!/usr/bin/env python3
"""Static site generator for portfolio website"""

import os
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from config import SITE_CONFIG


class PortfolioGenerator:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.template_dir = self.base_dir / 'templates'
        self.output_dir = self.base_dir / 'docs'
        self.static_dir = self.base_dir / 'static'
        
        # Setup Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            autoescape=True
        )
    
    def create_output_directory(self):
        """Create or clean the output directory"""
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True)
        print(f"✓ Created output directory: {self.output_dir}")
    
    def copy_static_files(self):
        """Copy static files (CSS, JS, images) to output directory"""
        if self.static_dir.exists():
            static_output = self.output_dir / 'static'
            shutil.copytree(self.static_dir, static_output)
            print(f"✓ Copied static files to: {static_output}")
    
    def render_template(self, template_name, context):
        """Render a template with the given context"""
        template = self.env.get_template(template_name)
        return template.render(config=SITE_CONFIG, **context)
    
    def generate_index(self):
        """Generate the index.html page"""
        html = self.render_template('index.html', {})
        output_file = self.output_dir / 'index.html'
        output_file.write_text(html)
        print(f"✓ Generated: {output_file}")
    
    def generate_projects(self):
        """Generate the projects page"""
        html = self.render_template('projects.html', {})
        output_file = self.output_dir / 'projects.html'
        output_file.write_text(html)
        print(f"✓ Generated: {output_file}")
    
    def generate_about(self):
        """Generate the about page"""
        html = self.render_template('about.html', {})
        output_file = self.output_dir / 'about.html'
        output_file.write_text(html)
        print(f"✓ Generated: {output_file}")
    
    def generate_404(self):
        """Generate the 404 error page"""
        html = self.render_template('404.html', {})
        output_file = self.output_dir / '404.html'
        output_file.write_text(html)
        print(f"✓ Generated: {output_file}")
    
    def generate_resume(self):
        """Generate the resume page"""
        html = self.render_template('resume.html', {})
        output_file = self.output_dir / 'resume.html'
        output_file.write_text(html)
        print(f"✓ Generated: {output_file}")
    
    def generate_blog(self):
        """Generate the blog page"""
        html = self.render_template('blog.html', {})
        output_file = self.output_dir / 'blog.html'
        output_file.write_text(html)
        print(f"✓ Generated: {output_file}")
    
    def generate_insights(self):
        """Generate the insights page"""
        html = self.render_template('insights.html', {})
        output_file = self.output_dir / 'insights.html'
        output_file.write_text(html)
        print(f"✓ Generated: {output_file}")
    
    def generate_insights_embed_table(self):
        """Generate embeddable insights table"""
        with open(self.template_dir / 'insights-embed-table.html', 'r') as f:
            html = f.read()
        output_file = self.output_dir / 'insights-embed-table.html'
        output_file.write_text(html)
        print(f"✓ Generated: {output_file}")
    
    def build(self):
        """Build the entire site"""
        print("🔨 Building portfolio website...\n")
        self.create_output_directory()
        self.copy_static_files()
        self.generate_index()
        self.generate_projects()
        self.generate_blog()
        self.generate_insights()
        self.generate_insights_embed_table()
        self.generate_resume()
        self.generate_about()
        self.generate_404()
        print("\n✅ Build complete! Output in: docs/")


def main():
    generator = PortfolioGenerator()
    generator.build()


if __name__ == '__main__':
    main()
