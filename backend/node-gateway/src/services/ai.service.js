/**
 * DeepSeek AI Service
 * Handles automated question generation and report analysis
 */

const axios = require('axios');
const logger = require('../config/logger');

const API_KEY = process.env.DEEPSEEK_API_KEY;
const MODEL = process.env.DEEPSEEK_MODEL || 'deepseek-chat';
const API_URL = process.env.DEEPSEEK_API_URL || 'https://api.deepseek.com/v1/chat/completions';

async function callDeepSeek(systemPrompt, userPrompt, maxTokens = 2000) {
  try {
    const response = await axios.post(API_URL, {
      model: MODEL,
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt },
      ],
      max_tokens: maxTokens,
      temperature: 0.7,
      response_format: { type: 'json_object' },
    }, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${API_KEY}`,
      },
      timeout: 30000,
    });

    const content = response.data.choices[0].message.content;
    return JSON.parse(content);
  } catch (err) {
    logger.error('DeepSeek API error:', err.response?.data || err.message);
    return null;
  }
}

// ─── AI Question Generator ───────────────────────────────────────
async function generateQuestions(framework, categories, depth, countPerCategory) {
  const systemPrompt = `You are a GRC compliance expert. Generate compliance assessment questions.
Return ONLY valid JSON matching this exact structure:
{
  "sections": [
    {
      "section": "Category Name",
      "questions": [
        {
          "text": "Question text here?",
          "hint": "Guidance for the assessor",
          "options": ["Yes -- fully implemented and documented", "Partially implemented", "In draft or planning stage", "Not implemented"]
        }
      ]
    }
  ]
}

Rules:
- Each section must have exactly the number of questions specified
- Questions must be specific to the framework
- Options must always be the 4 options shown (best to worst)
- No extra text, only JSON`;

  const userPrompt = `Generate compliance questions for:
Framework: ${framework}
Categories: ${categories.map(c => `${c.name} (${c.count} questions each)`).join(', ')}
Depth: ${depth} (quick=brief, intermediate=balanced, deep=thorough)

Return JSON with sections array.`;

  const result = await callDeepSeek(systemPrompt, userPrompt, 3000);
  return result;
}

// ─── AI Report Generator ─────────────────────────────────────────
async function generateReport(framework, score, risk, gaps, answers) {
  const systemPrompt = `You are a GRC analyst AI. Generate a compliance assessment report.
Return ONLY valid JSON matching this exact structure:
{
  "executive_summary": "2-3 paragraph summary",
  "key_findings": ["finding 1", "finding 2", "finding 3"],
  "risk_analysis": {
    "overall_risk": "Low/Medium/High/Critical",
    "risk_factors": [{"factor": "name", "severity": "low/medium/high/critical", "description": "details"}]
  },
  "recommendations": [
    {"title": "title", "detail": "description", "priority": "critical/high/medium/low", "effort": "high/medium/low", "estimated_cost_inr": 50000}
  ],
  "cyber_insurance": {"level": "Required/Recommended/Optional", "coverage": "$X - $Y", "reason": "why"},
  "implementation_timeline": {
    "immediate": {"label": "0-3 months", "items": 3, "cost_inr": 100000},
    "short_term": {"label": "3-6 months", "items": 2, "cost_inr": 75000},
    "long_term": {"label": "6-12 months", "items": 1, "cost_inr": 50000}
  }
}

Rules:
- Be specific to the framework
- Cost estimates in INR
- 3-5 recommendations minimum
- No extra text, only JSON`;

  const gapSummary = gaps.slice(0, 10).map(g => `${g.control_name || g.domain}: ${g.current_state} (severity: ${g.gap_severity})`).join('\n');

  const userPrompt = `Generate compliance report for:
Framework: ${framework}
Overall Score: ${score}%
Risk Level: ${risk}
Total Gaps: ${gaps.length}

Top Gaps:
${gapSummary || 'No gaps identified'}

Return JSON report.`;

  return callDeepSeek(systemPrompt, userPrompt, 4000);
}

module.exports = { generateQuestions, generateReport, callDeepSeek };
