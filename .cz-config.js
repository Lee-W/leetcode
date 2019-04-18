/**
 * @license Copyright 2017 Google Inc. All Rights Reserved.
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
 */
'use strict';

module.exports = {
  allowBreakingChanges: ['core'],
  allowCustomScopes: true,
  scopes: [],
  types: [
    {
      value: 'problem',
      name: 'problem:   New roblem solved'
    },
    {
      value: 'testcase',
      name: 'testcase:    New testcase added'
    },
    {
      value: 'perf',
      name: 'perf:     A code change that improves performance'
    },
    {
      value: 'fix',
      name: 'fix:      A bug fix'
    },
    {
      value: 'docs',
      name: 'docs:     Documentation only changes'
    },
    {
      value: 'style',
      name: 'style:    Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)'
    },
    {
      value: 'refactor',
      name: 'refactor: A code change that neither fixes a bug nor adds a feature'
    },
    {
      value: 'build',
      name: 'build:    Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)'
    },
    {
      value: 'chore',
      name: 'chore:    Other changes that don\'t modify src or test files'
    },
    {
      value: 'revert',
      name: 'revert:   Reverts a previous commit'
    }
  ]
};