# AI Test Paper Generator

An AI agent designed to generate practice test papers from past-year questions and syllabus outlines. The goal is to help students create extra relevant revision materials that reflect the topics, question styles, and difficulty of previous assessments.

## Project Idea

The agent aims to combine two sources of information:

- **Past-year questions** to identify recurring topics, question formats, and assessment patterns.
- **Syllabus outlines** to define the scope of the generated paper and keep questions aligned with the intended curriculum.

Using these inputs, the agent would generate new practice questions rather than simply reproduce an existing paper. Generated papers are intended for revision and practice, not as predictions of future examinations.

## Intended Workflow

1. Provide past-year questions and the relevant syllabus outline.
2. Specify preferences such as topics, difficulty, and paper length.
3. Have the agent analyze the material and generate a practice paper.
4. Review and refine the output for accuracy, clarity, and syllabus coverage.

## API Access and Configuration
Development and testing uses the Google Gemini API, with my API credentials configured locally. Those credentials are private and are not included in this repository. 
**Anyone cloning or using this project must provide and configure their own API access.** This repository does not provide a shared API key or hosted AI service.
You may use your own Gemini credentials. Using another cloud provider or a locally hosted model may require adapting the API integration to match that provider's interface. Any usage costs and provider limits depend on your chosen setup.
Keep API keys and other credentials outside version control, using environment variables or an untracked local configuration file.

## Development Status
This project is being developed as a prototype. The workflow above describes the intended direction; available features will depend on the current implementation.
AI-generated questions should be reviewed before use, especially when checking factual accuracy, difficulty, and alignment with the syllabus.
