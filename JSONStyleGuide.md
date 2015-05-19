


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>google-styleguide/JSONStyleGuide.md at master · darcyliu/google-styleguide</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="darcyliu/google-styleguide" name="twitter:title" /><meta content="google-styleguide - Mirror of &amp;quot;Style guides for Google-originated open-source projects&amp;quot;" name="twitter:description" /><meta content="https://avatars0.githubusercontent.com/u/384589?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars0.githubusercontent.com/u/384589?v=3&amp;s=400" property="og:image" /><meta content="darcyliu/google-styleguide" property="og:title" /><meta content="https://github.com/darcyliu/google-styleguide" property="og:url" /><meta content="google-styleguide - Mirror of &quot;Style guides for Google-originated open-source projects&quot;" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/NTY3NDc0NDpkYjA2YTlmNmYzZjgwZWQ0MzM5OTViYzU1NGJkY2NhNjplNmE3NDhhNTZmNTQ3MGNmMThhNTg0M2RiNWU5M2RmNzQ0ZDAwZGMzZDAwMDU4MmViYjAyYWI5ZmUxZWU4YTgz--de608b91fc2bc73b715609d957e8893d8b72442b">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="6A269F94:4044:136EC1E:555B207F" name="octolytics-dimension-request_id" /><meta content="5674744" name="octolytics-actor-id" /><meta content="xiangxing98" name="octolytics-actor-login" /><meta content="544863faa15bf165434cdc337641330753765f53d6164f189e8760be65cb9a8d" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />
    <meta class="js-ga-set" name="dimension1" content="Logged In">
    <meta class="js-ga-set" name="dimension2" content="Header v3">
    <meta name="is-dotcom" content="true">
      <meta name="hostname" content="github.com">
    <meta name="user-login" content="xiangxing98">

    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="VLUQ4SOS9AGp2m4H5XTvmaRYP1TpkA0CHLqw64GeVSDKnEc/Q1H6hNCqj0kLf9rGeLy5DNhcDAQNDs+fZwm1pw==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github/index-d80e093fe7c48ff920ce83dfd2ad7c02806722220d164b49101ed783098ea618.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2/index-99a58ea750b0547d1266460cd4ade0c2c81ed8c524cbba4ea5e3b37e18daec79.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="7bc30b38b669884142fe7da73f3839dd">

      
  <meta name="description" content="google-styleguide - Mirror of &quot;Style guides for Google-originated open-source projects&quot;">
  <meta name="go-import" content="github.com/darcyliu/google-styleguide git https://github.com/darcyliu/google-styleguide.git">

  <meta content="384589" name="octolytics-dimension-user_id" /><meta content="darcyliu" name="octolytics-dimension-user_login" /><meta content="4376755" name="octolytics-dimension-repository_id" /><meta content="darcyliu/google-styleguide" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="4376755" name="octolytics-dimension-repository_network_root_id" /><meta content="darcyliu/google-styleguide" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/darcyliu/google-styleguide/commits/master.atom" rel="alternate" title="Recent Commits to google-styleguide:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      


        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/darcyliu/google-styleguide/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/darcyliu/google-styleguide/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <label class="js-chromeless-input-container form-control">
    <div class="scope-badge">This repository</div>
    <input type="text"
      class="js-site-search-focus js-site-search-field is-clearable chromeless-input"
      data-hotkey="s"
      name="q"
      placeholder="Search"
      data-global-scope-placeholder="Search GitHub"
      data-repo-scope-placeholder="Search"
      tabindex="1"
      autocapitalize="off">
  </label>
</form>
      </div>

      <ul class="header-nav left" role="navigation">
          <li class="header-nav-item explore">
            <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
          </li>
            <li class="header-nav-item">
              <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
            </li>
            <li class="header-nav-item">
              <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
            </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
          </li>
      </ul>

      
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/xiangxing98" data-ga-click="Header, go to profile, text:username">
      <img alt="@xiangxing98" class="avatar" data-user="5674744" height="20" src="https://avatars2.githubusercontent.com/u/5674744?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">xiangxing98</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="/new" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu">
        
<li>
  <a href="/new" data-ga-click="Header, create new repository, icon:repo"><span class="octicon octicon-repo"></span> New repository</a>
</li>
<li>
  <a href="/organizations/new" data-ga-click="Header, create new organization, icon:organization"><span class="octicon octicon-organization"></span> New organization</a>
</li>


  <li class="dropdown-divider"></li>
  <li class="dropdown-header">
    <span title="darcyliu/google-styleguide">This repository</span>
  </li>
    <li>
      <a href="/darcyliu/google-styleguide/issues/new" data-ga-click="Header, create new issue, icon:issue"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>

      </ul>
    </div>
  </li>

  <li class="header-nav-item">
      <span class="js-socket-channel js-updatable-content"
        data-channel="notification-changed:xiangxing98"
        data-url="/notifications/header">
      <a href="/notifications" aria-label="You have unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:unread" data-hotkey="g n">
          <span class="mail-status unread"></span>
          <span class="octicon octicon-inbox"></span>
</a>  </span>

  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="ep2BvzuRy/n5+BrbfPezozrM5/kKOABVPHRs4z+Y6k+ojV0Fvwp1SaVI+gE1XentExDWvQoopliiy98GZkCgGQ==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>



    
  </div>
</div>

        

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="RUBtsq/FpqeQf4UI/0WTCEJrzmVd7kebh3B/6kt63Qy/F1kNeM5uodpfMPzK/2K+8CkY1DETs16burDJUZhx7Q==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="4376755" />

      <div class="select-menu js-menu-container js-select-menu">
        <a href="/darcyliu/google-styleguide/subscription"
          class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
          data-ga-click="Repository, click Watch settings, action:blob#show">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Watch
          </span>
        </a>
        <a class="social-count js-social-count" href="/darcyliu/google-styleguide/watchers">
          72
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/darcyliu/google-styleguide/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Z8rGl9cJ2/Fq/vlsDAgv//SLq9UYOoW+czX0kKAypzs4w18sXGuXuNJ0BPCvpksK0mYv/a57UvMoJyl7BgG6ow==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar darcyliu/google-styleguide"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/darcyliu/google-styleguide/stargazers">
          410
        </a>
</form>
    <form accept-charset="UTF-8" action="/darcyliu/google-styleguide/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="eKlg3LXLeI2EursWeVOtZ6KnMDYoHKj0CsUe2+hLrygCtQJdYOFU0BvkelzQe8O5C9UWa9+KJslQnujLQUuE8Q==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star darcyliu/google-styleguide"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/darcyliu/google-styleguide/stargazers">
          410
        </a>
</form>  </div>

  </li>

        <li>
          <form accept-charset="UTF-8" action="/darcyliu/google-styleguide/fork" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="VPGZxN/SgwHXlsKVq6+PsfW/wLeYXJGgvIsRJrwsfOnzOhVCJ+GddXEmw7DKtDCOHYfUbti1JyfLnUW0c4tWgQ==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of darcyliu/google-styleguide to your account"
                aria-label="Fork your own copy of darcyliu/google-styleguide to your account">
              <span class="octicon octicon-repo-forked"></span>
              Fork
            </button>
            <a href="/darcyliu/google-styleguide/network" class="social-count">126</a>
</form>        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/darcyliu" class="url fn" itemprop="url" rel="author"><span itemprop="title">darcyliu</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/darcyliu/google-styleguide" class="js-current-repository" data-pjax="#js-repo-pjax-container">google-styleguide</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/darcyliu/google-styleguide/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/darcyliu/google-styleguide" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /darcyliu/google-styleguide">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/darcyliu/google-styleguide/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /darcyliu/google-styleguide/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/darcyliu/google-styleguide/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /darcyliu/google-styleguide/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/darcyliu/google-styleguide/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /darcyliu/google-styleguide/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/darcyliu/google-styleguide/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /darcyliu/google-styleguide/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/darcyliu/google-styleguide/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /darcyliu/google-styleguide/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/darcyliu/google-styleguide.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:darcyliu/google-styleguide.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/darcyliu/google-styleguide" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>, <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>, or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="github-windows://openRepo/https://github.com/darcyliu/google-styleguide" class="btn btn-sm sidebar-button" title="Save darcyliu/google-styleguide to your computer and use it in GitHub Desktop." aria-label="Save darcyliu/google-styleguide to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>


                <a href="/darcyliu/google-styleguide/archive/master.zip"
                   class="btn btn-sm sidebar-button"
                   aria-label="Download the contents of darcyliu/google-styleguide as a zip file"
                   title="Download the contents of darcyliu/google-styleguide as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>

          

<a href="/darcyliu/google-styleguide/blob/7c55f123af10260062457bbf8f63c8452c95bcaf/JSONStyleGuide.md" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:bd4b994c397a9dd36914f0fca6d94172 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/darcyliu/google-styleguide/blob/master/JSONStyleGuide.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/darcyliu/google-styleguide/find/master"
          class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/darcyliu/google-styleguide" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">google-styleguide</span></a></span></span><span class="separator">/</span><strong class="final-path">JSONStyleGuide.md</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="Yang Pengcheng" class="avatar" data-user="3127508" height="24" src="https://avatars2.githubusercontent.com/u/3127508?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/nail1208" rel="contributor">nail1208</a></span>
        <time datetime="2013-07-14T16:31:12Z" is="relative-time">Jul 15, 2013</time>
        <div class="commit-title">
            <a href="/darcyliu/google-styleguide/commit/4234b55be09bc97acb732c3be5bc36a3bbf751eb" class="message" data-pjax="true" title="Update JSONStyleGuide.md

unicode">Update JSONStyleGuide.md</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>3</strong>
           contributors
        </a>
      </p>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="darcyliu" href="/darcyliu/google-styleguide/commits/master/JSONStyleGuide.md?author=darcyliu"><img alt="Darcy Liu" class="avatar" data-user="384589" height="20" src="https://avatars2.githubusercontent.com/u/384589?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="nail1208" href="/darcyliu/google-styleguide/commits/master/JSONStyleGuide.md?author=nail1208"><img alt="Yang Pengcheng" class="avatar" data-user="3127508" height="20" src="https://avatars0.githubusercontent.com/u/3127508?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="kingheaven" href="/darcyliu/google-styleguide/commits/master/JSONStyleGuide.md?author=kingheaven"><img alt="David Xie" class="avatar" data-user="100747" height="20" src="https://avatars0.githubusercontent.com/u/100747?v=3&amp;s=40" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Darcy Liu" data-user="384589" height="24" src="https://avatars0.githubusercontent.com/u/384589?v=3&amp;s=48" width="24" />
            <a href="/darcyliu">darcyliu</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Yang Pengcheng" data-user="3127508" height="24" src="https://avatars2.githubusercontent.com/u/3127508?v=3&amp;s=48" width="24" />
            <a href="/nail1208">nail1208</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="David Xie" data-user="100747" height="24" src="https://avatars2.githubusercontent.com/u/100747?v=3&amp;s=48" width="24" />
            <a href="/kingheaven">kingheaven</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="/darcyliu/google-styleguide/raw/master/JSONStyleGuide.md" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="/darcyliu/google-styleguide/blame/master/JSONStyleGuide.md" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="/darcyliu/google-styleguide/commits/master/JSONStyleGuide.md" class="btn btn-sm " rel="nofollow">History</a>
      </div>

        <a class="octicon-btn tooltipped tooltipped-nw"
           href="github-windows://openRepo/https://github.com/darcyliu/google-styleguide?branch=master&amp;filepath=JSONStyleGuide.md"
           aria-label="Open this file in GitHub for Windows"
           data-ga-click="Repository, open with desktop, type:windows">
            <span class="octicon octicon-device-desktop"></span>
        </a>

            <form accept-charset="UTF-8" action="/darcyliu/google-styleguide/edit/master/JSONStyleGuide.md" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Xm3bB64xdlmkITWazP+VGxCGAflwx+D2RhYNoHtaoL/mpNtk92uiX9N+Yd5zERl+uoT1pKutaWGRmvZv4hSznA==" /></div>
              <button class="octicon-btn tooltipped tooltipped-n" type="submit" aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
                <span class="octicon octicon-pencil"></span>
              </button>
</form>
          <form accept-charset="UTF-8" action="/darcyliu/google-styleguide/delete/master/JSONStyleGuide.md" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="vzv4ctuBJ7gOItgp4ZaLCeozPgx7ZNpveY2uqS5387wVwgER4air3mnP9UM+UitWWO5wEgpZ5Itnavw8/1Nuxw==" /></div>
            <button class="octicon-btn octicon-btn-danger tooltipped tooltipped-n" type="submit" aria-label="Fork this project and delete this file" data-disable-with>
              <span class="octicon octicon-trashcan"></span>
            </button>
</form>    </div>

    <div class="file-info">
        1103 lines (793 sloc)
        <span class="file-info-divider"></span>
      33.881 kb
    </div>
  </div>
    <div id="readme" class="blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="mainContentOfPage"><h1>
<a id="user-content-json风格指南" class="anchor" href="#json%E9%A3%8E%E6%A0%BC%E6%8C%87%E5%8D%97" aria-hidden="true"><span class="octicon octicon-link"></span></a>JSON风格指南</h1>

<p>版本：0.9</p>

<p>英文版：<a href="http://google-styleguide.googlecode.com/svn/trunk/jsoncstyleguide.xml">http://google-styleguide.googlecode.com/svn/trunk/jsoncstyleguide.xml</a></p>

<p>翻译：Darcy Liu</p>

<p>译文状态：草稿</p>

<h2>
<a id="user-content-简介" class="anchor" href="#%E7%AE%80%E4%BB%8B" aria-hidden="true"><span class="octicon octicon-link"></span></a>简介</h2>

<p>该风格指南是对在Google创建JSON APIs而提供的指导性准则和建议。总体来讲，JSON APIs应遵循JSON.org上的规范。这份风格指南澄清和标准化了特定情况，从而使Google的JSON APIs有一种标准的外观和感觉。这些指南适用于基于RPC和基于REST风格的API的JSON请求和响应。</p>

<h2>
<a id="user-content-定义" class="anchor" href="#%E5%AE%9A%E4%B9%89" aria-hidden="true"><span class="octicon octicon-link"></span></a>定义</h2>

<p>为了更好地实现这份风格指南的目的，下面几项需要说明：</p>

<ul>
<li>属性(property) - JSON对象内的键值对(name/value pair)</li>
<li>属性名(property name) - 属性的名称(或键)</li>
<li>属性值(property value) - 分配给属性的值</li>
</ul>

<p>示例：</p>

<pre><code>{
  // 一组键值对称作一个 "属性".
  "propertyName": "propertyValue"
}
</code></pre>

<p>Javascript的数字(<em>number</em>)包含所有的浮点数,这是一个宽泛的指定。在这份指南中，数字(<em>number</em>)指代Javascript中的数字(<em>number</em>)类型，而整型(<em>integer</em>)则指代整型。</p>

<h2>
<a id="user-content-一般准则" class="anchor" href="#%E4%B8%80%E8%88%AC%E5%87%86%E5%88%99" aria-hidden="true"><span class="octicon octicon-link"></span></a>一般准则</h2>

<h3>
<a id="user-content-注释" class="anchor" href="#%E6%B3%A8%E9%87%8A" aria-hidden="true"><span class="octicon octicon-link"></span></a>注释</h3>

<p><strong>JSON对象中不包含注释。</strong></p>

<p>JSON对象中不应该包含注释。该指南中的某些示例含有注释。但这仅仅是为了说明示例。</p>

<pre><code>{
  // 你可能在下面的示例中看到注释,
  // 但不要在你的JSON数据中加入注释.
  "propertyName": "propertyValue"
}
</code></pre>

<h3>
<a id="user-content-双引号" class="anchor" href="#%E5%8F%8C%E5%BC%95%E5%8F%B7" aria-hidden="true"><span class="octicon octicon-link"></span></a>双引号</h3>

<p><strong>使用双引号</strong></p>

<p>如果（某个）属性需要引号，则必须使用双引号。所有的属性名必须在双引号内。字符类型的属性值必须使用双引号。其它类型值（如布尔或数字）不应该使用双引号。</p>

<h3>
<a id="user-content-扁平化数据-vs-结构层次" class="anchor" href="#%E6%89%81%E5%B9%B3%E5%8C%96%E6%95%B0%E6%8D%AE-vs-%E7%BB%93%E6%9E%84%E5%B1%82%E6%AC%A1" aria-hidden="true"><span class="octicon octicon-link"></span></a>扁平化数据 VS 结构层次</h3>

<p><strong>不能为了方便而将数据任意分组</strong></p>

<p>JSON中的数据元素应以<em>扁平化</em>方式呈现。不能为了方便而将数据任意分组。</p>

<p>在某些情况下，比如描述单一结构的一批属性，因为它被用来保持结构层次，因而是有意义的。但是遇到这些情况还是应当慎重考虑，记住只有语义上有意义的时候才使用它。例如，一个地址可以有表示两种方式，但结构化的方式对开发人员来讲可能更有意义：</p>

<p>扁平化地址:</p>

<pre><code>{
  "company": "Google",
  "website": "http://www.google.com/",
  "addressLine1": "111 8th Ave",
  "addressLine2": "4th Floor",
  "state": "NY",
  "city": "New York",
  "zip": "10011"
}
</code></pre>

<p>结构化地址：</p>

<pre><code>{
  "company": "Google",
  "website": "http://www.google.com/",
  "address": {
    "line1": "111 8th Ave",
    "line2": "4th Floor",
    "state": "NY",
    "city": "New York",
    "zip": "10011"
  }
}
</code></pre>

<h2>
<a id="user-content-属性名准则" class="anchor" href="#%E5%B1%9E%E6%80%A7%E5%90%8D%E5%87%86%E5%88%99" aria-hidden="true"><span class="octicon octicon-link"></span></a>属性名准则</h2>

<h3>
<a id="user-content-属性名格式" class="anchor" href="#%E5%B1%9E%E6%80%A7%E5%90%8D%E6%A0%BC%E5%BC%8F" aria-hidden="true"><span class="octicon octicon-link"></span></a>属性名格式</h3>

<p><strong>选择有意义的属性名</strong></p>

<p>属性名必须遵循以下准则:</p>

<ul>
<li>属性名应该是具有定义语义的有意义的名称。</li>
<li>属性名必须是驼峰式的，ASCII码字符串。</li>
<li>首字符必须式字母，下划线(<em>_</em>)或美元符号(<em>$</em>)。</li>
<li>随后的其他字符可以是字母，数字，下划线(<em>_</em>)或美元符号(<em>$</em>)。</li>
<li>应该避免使用Javascript中的保留关键字(下文附有Javascript保留字清单)</li>
</ul>

<p>这些准则反映JavaScript标识符命名的指导方针。使JavaScript的客户端可以使用点符号来访问属性。(例如, <code>result.thisIsAnInstanceVariable</code>). </p>

<p>下面是一个对象的一个属性的例子：</p>

<pre><code>{
  "thisPropertyIsAnIdentifier": "identifier value"
}
</code></pre>

<h3>
<a id="user-content-json-map中的键名" class="anchor" href="#json-map%E4%B8%AD%E7%9A%84%E9%94%AE%E5%90%8D" aria-hidden="true"><span class="octicon octicon-link"></span></a>JSON Map中的键名</h3>

<p><strong>在JSON Map中键名可以使用任意Unicode字符</strong></p>

<p>当JSON对象作为Map(映射)使用时，属性的名称命名规则并不适用。Map（也称作关联数组）是一个具有任意键/值对的数据类型，这些键/值对通过特定的键来访问相应的值。JSON对象和JSON Map在运行时看起来是一样的；这个特性与API设计相关。当JSON对象被当作map使用时，API文件应当做出说明。</p>

<p>Map的键名不一定要遵循属性名称的命名准则。键名可以包含任意的Unicode字符。客户端可使用maps熟悉的方括号来访问这些属性。（例如<code>result.thumbnails["72"]</code>）</p>

<pre><code>{
  // "address" 属性是一个子对象
  // 包含地址的各部分.
  "address": {
    "addressLine1": "123 Anystreet",
    "city": "Anytown",
    "state": "XX",
    "zip": "00000"
  },
  // "address" 是一个映射
  // 含有响应规格所对应的URL，用来映射thumbnail url的像素规格
  "thumbnails": {
    "72": "http://url.to.72px.thumbnail",
    "144": "http://url.to.144px.thumbnail"
  }
}
</code></pre>

<h3>
<a id="user-content-保留的属性名称" class="anchor" href="#%E4%BF%9D%E7%95%99%E7%9A%84%E5%B1%9E%E6%80%A7%E5%90%8D%E7%A7%B0" aria-hidden="true"><span class="octicon octicon-link"></span></a>保留的属性名称</h3>

<p><strong>某些属性名称会被保留以便能在多个服务间相容使用</strong></p>

<p>保留属性名称的详细信息，连同完整的列表，可在本指南后面的内容中找到。服务应按照被定义的语义来使用属性名称。</p>

<h3>
<a id="user-content-单数属性名-vs-复数属性名" class="anchor" href="#%E5%8D%95%E6%95%B0%E5%B1%9E%E6%80%A7%E5%90%8D-vs-%E5%A4%8D%E6%95%B0%E5%B1%9E%E6%80%A7%E5%90%8D" aria-hidden="true"><span class="octicon octicon-link"></span></a>单数属性名 VS 复数属性名</h3>

<p><strong>数组类型应该是复数属性名。其它属性名都应该是单数。</strong></p>

<p>数组通常包含多个条目，复数属性名就反映了这点。在下面这个保留名称中可以看到例子。属性名<em>items</em>是复数因为它描述的是一组对象。大多数的其它字段是单数。</p>

<p>当然也有例外，尤其是涉及到数字的属性值的时候。例如，在保留属性名中，<em>totalItems</em> 比 <em>totalItem</em>更合理。然后，从技术上讲，这并不违反风格指南，因为 <em>totalItems</em> 可以被看作 <em>totalOfItems</em>, 其中 <em>total</em> 是单数（依照风格指南），<em>OfItems</em> 用来限定总数。字段名也可被改为 <em>itemCount</em>，这样看起来更象单数.</p>

<pre><code>{
  // 单数
  "author": "lisa",
  // 一组同胞, 复数
  "siblings": [ "bart", "maggie"],
  // "totalItem" 看起来并不对
  "totalItems": 10,
  // 但 "itemCount" 要好些
  "itemCount": 10,
}
</code></pre>

<h3>
<a id="user-content-命名冲突" class="anchor" href="#%E5%91%BD%E5%90%8D%E5%86%B2%E7%AA%81" aria-hidden="true"><span class="octicon octicon-link"></span></a>命名冲突</h3>

<p><strong>通过选择新的属性名或将API版本化来避免命名冲突</strong></p>

<p>新的属性可在将来被添加进保留列表中。JSON中不存在命名空间。如果存在命名冲突，可通过选择新的属性名或者版本化来解决这个问题。例如，假设我们由下面的JSON对象开始：</p>

<pre><code>{
  "apiVersion": "1.0",
  "data": {
    "recipeName": "pizza",
    "ingredients": ["tomatoes", "cheese", "sausage"]
  }
}
</code></pre>

<p>如果我们希望将来把<em>ingredients</em>列为保留字，我们可以通过下面两件事情来达成。
1.选一个不同的名字</p>

<pre><code>{
  "apiVersion": "1.0",
  "data": {
    "recipeName": "pizza",
    "ingredientsData": "Some new property",
    "ingredients": ["tomatoes", "cheese", "sausage"]
  }
}
</code></pre>

<p>2.在主版本上重新命名属性</p>

<pre><code>{
  "apiVersion": "2.0",
  "data": {
    "recipeName": "pizza",
    "ingredients": "Some new property",
    "recipeIngredients": ["tomatos", "cheese", "sausage"]
  }
}
</code></pre>

<h2>
<a id="user-content-属性值准则" class="anchor" href="#%E5%B1%9E%E6%80%A7%E5%80%BC%E5%87%86%E5%88%99" aria-hidden="true"><span class="octicon octicon-link"></span></a>属性值准则</h2>

<h3>
<a id="user-content-属性值格式" class="anchor" href="#%E5%B1%9E%E6%80%A7%E5%80%BC%E6%A0%BC%E5%BC%8F" aria-hidden="true"><span class="octicon octicon-link"></span></a>属性值格式</h3>

<p><strong>属性值必须是Unicode 的 booleans（布尔）, 数字(numbers), 字符串(strings), 对象(objects), 数组(arrays), 或 null.</strong></p>

<p>JSON.org上的标准准确的说明了哪些类型的数据可以作为属性值。这包含Unicode的布尔(booleans), 数字(numbers), 字符串(strings), 对象(objects), 数组(arrays), 或 null。JavaScript表达式是不被接受的。APIs应该支持该准则，并为某个特定的属性选择最合适的数据类型（比如，用numbers代表numbers等）。</p>

<p>好的例子：</p>

<pre><code>{
  "canPigsFly": null,     // null
  "areWeThereYet": false, // boolean
  "answerToLife": 42,     // number
  "name": "Bart",         // string
  "moreData": {},         // object
  "things": []            // array
}
</code></pre>

<p>不好的例子：</p>

<pre><code>{
  "aVariableName": aVariableName,         // Bad - JavaScript 标识符
  "functionFoo": function() { return 1; } // Bad - JavaScript 函数
}
</code></pre>

<h3>
<a id="user-content-空或null-属性值" class="anchor" href="#%E7%A9%BA%E6%88%96null-%E5%B1%9E%E6%80%A7%E5%80%BC" aria-hidden="true"><span class="octicon octicon-link"></span></a>空或Null 属性值</h3>

<p><strong>考虑移除空或null值</strong></p>

<p>如果一个属性是可选的或者包含空值或<em>null</em>值，考虑从JSON中去掉该属性，除非它的存在有很强的语义原因。</p>

<pre><code>{
  "volume": 10,

  // 即使 "balance" 属性值是零, 它也应当被保留,
  // 因为 "0" 表示 "均衡" 
  // "-1" 表示左倾斜和"＋1" 表示右倾斜
  "balance": 0,

  // "currentlyPlaying" 是null的时候可被移除
  // "currentlyPlaying": null
}
</code></pre>

<h3>
<a id="user-content-枚举值" class="anchor" href="#%E6%9E%9A%E4%B8%BE%E5%80%BC" aria-hidden="true"><span class="octicon octicon-link"></span></a>枚举值</h3>

<p><strong>枚举值应当以字符串的形式呈现</strong></p>

<p>随着APIs的发展，枚举值可能被添加，移除或者改变。将枚举值当作字符串可以使下游用户幽雅的处理枚举值的变更。</p>

<p>Java代码：</p>

<pre><code>public enum Color {
  WHITE,
  BLACK,
  RED,
  YELLOW,
  BLUE
}
</code></pre>

<p>JSON对象：</p>

<pre><code>{
  "color": "WHITE"
}
</code></pre>

<h2>
<a id="user-content-属性值数据类型" class="anchor" href="#%E5%B1%9E%E6%80%A7%E5%80%BC%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B" aria-hidden="true"><span class="octicon octicon-link"></span></a>属性值数据类型</h2>

<p>上面提到，属性值必须是布尔(booleans), 数字(numbers), 字符串(strings), 对象(objects), 数组(arrays), 或 null. 然而在处理某些值时，定义一组标准的数据类型是非常有用的。这些数据类型必须始终是字符串，但是为了便于解析，它们也会以特定的方式被格式化。</p>

<h3>
<a id="user-content-日期属性值" class="anchor" href="#%E6%97%A5%E6%9C%9F%E5%B1%9E%E6%80%A7%E5%80%BC" aria-hidden="true"><span class="octicon octicon-link"></span></a>日期属性值</h3>

<p><strong>日期应该使用RFC3339建议的格式</strong></p>

<p>日期应该是RFC 3339所建议的字符串格式。</p>

<pre><code>{
  "lastUpdate": "2007-11-06T16:34:41.000Z"
}
</code></pre>

<h3>
<a id="user-content-时间间隔属性值" class="anchor" href="#%E6%97%B6%E9%97%B4%E9%97%B4%E9%9A%94%E5%B1%9E%E6%80%A7%E5%80%BC" aria-hidden="true"><span class="octicon octicon-link"></span></a>时间间隔属性值</h3>

<p><strong>时间间隔应该使用ISO 8601建议的格式</strong></p>

<p>时间间隔应该是ISO 8601所建议的字符串格式。</p>

<pre><code>{
  // 三年, 6个月, 4天, 12小时,
  // 三十分钟, 5秒
  "duration": "P3Y6M4DT12H30M5S"
}
</code></pre>

<h3>
<a id="user-content-纬度经度属性值" class="anchor" href="#%E7%BA%AC%E5%BA%A6%E7%BB%8F%E5%BA%A6%E5%B1%9E%E6%80%A7%E5%80%BC" aria-hidden="true"><span class="octicon octicon-link"></span></a>纬度/经度属性值</h3>

<p><strong>纬度/经度应该使用ISO 6709建议的格式</strong></p>

<p>纬度/经度应该是ISO 6709所建议的字符串格式。
而且, 它应该更偏好使用 e Â±DD.DDDDÂ±DDD.DDDD 角度格式.</p>

<pre><code>{
  // 自由女神像的纬度/经度位置.
  "statueOfLiberty": "+40.6894-074.0447"
}
</code></pre>

<h2>
<a id="user-content-json结构和保留属性名" class="anchor" href="#json%E7%BB%93%E6%9E%84%E5%92%8C%E4%BF%9D%E7%95%99%E5%B1%9E%E6%80%A7%E5%90%8D" aria-hidden="true"><span class="octicon octicon-link"></span></a>JSON结构和保留属性名</h2>

<p>为了使APIs保持一致的借口，JSON对象应当使用以下的结构。该结构适用于JSON的请求和响应。在这个结构中，某些属性名将被保留用作特殊用途。这些属性并不是必需的，也就是说，每个保留的属性可能出现零次或一次。但是如果服务需要这些属性，建议遵循该命名条约。下面是一份JSON结构语义表，以Orderly格式呈现(现在已经被纳入 JSONSchema)。你可以在该指南的最后找到关于JSON结构的例子。</p>

<pre><code>object {
  string apiVersion?;
  string context?;
  string id?;
  string method?;
  object {
    string id?
  }* params?;
  object {
    string kind?;
    string fields?;
    string etag?;
    string id?;
    string lang?;
    string updated?; # date formatted RFC 3339
    boolean deleted?;
    integer currentItemCount?;
    integer itemsPerPage?;
    integer startIndex?;
    integer totalItems?;
    integer pageIndex?;
    integer totalPages?;
    string pageLinkTemplate /^https?:/ ?;
    object {}* next?;
    string nextLink?;
    object {}* previous?;
    string previousLink?;
    object {}* self?;
    string selfLink?;
    object {}* edit?;
    string editLink?;
    array [
      object {}*;
    ] items?;
  }* data?;
  object {
    integer code?;
    string message?;
    array [
      object {
        string domain?;
        string reason?;
        string message?;
        string location?;
        string locationType?;
        string extendedHelp?;
        string sendReport?;
      }*;
    ] errors?;
  }* error?;
}*;
</code></pre>

<p>JSON对象有一些顶级属性，然后是<em>data</em>对象或<em>error</em>对象，这两者不会同时出现。下面是这些属性的解释。</p>

<h2>
<a id="user-content-顶级保留属性名称" class="anchor" href="#%E9%A1%B6%E7%BA%A7%E4%BF%9D%E7%95%99%E5%B1%9E%E6%80%A7%E5%90%8D%E7%A7%B0" aria-hidden="true"><span class="octicon octicon-link"></span></a>顶级保留属性名称</h2>

<p><strong>顶级的JSON对象可能包含下面这些属性</strong></p>

<h3>
<a id="user-content-apiversion" class="anchor" href="#apiversion" aria-hidden="true"><span class="octicon octicon-link"></span></a>apiVersion</h3>

<pre><code>属性值类型: 字符串(string)
父节点: -
</code></pre>

<p>呈现请求中服务API期望的版本，以及在响应中保存的服务API版本。应随时提供<em>apiVersion</em>。这与数据的版本无关。将数据版本化应该通过其他的机制来处理，如etag。</p>

<p>示例：</p>

<pre><code>{ "apiVersion": "2.1" }
</code></pre>

<h3>
<a id="user-content-context" class="anchor" href="#context" aria-hidden="true"><span class="octicon octicon-link"></span></a>context</h3>

<pre><code>属性值类型: 字符串(string)
父节点: -
</code></pre>

<p>客户端设置这个值，服务器通过数据作出回应。这在JSON-P和批处理中很有用，用户可以使用<em>context</em>将响应与请求关联起来。该属性是顶级属性，因为不管响应是成功还是有错误，<em>context</em>总应当被呈现出来。<em>context</em>不同于<em>id</em>在于<em>context</em>由用户提供而<em>id</em>由服务分配。</p>

<p>示例：</p>

<p>请求 #1:</p>

<pre><code>http://www.google.com/myapi?context=bart
</code></pre>

<p>请求 #2:</p>

<pre><code>http://www.google.com/myapi?context=lisa
</code></pre>

<p>响应 #1:</p>

<pre><code>{
  "context": "bart",
  "data": {
    "items": []
  }
}
</code></pre>

<p>响应 #2:</p>

<pre><code>{
  "context": "lisa",
  "data": {
    "items": []
  }
}
</code></pre>

<p>公共的JavaScript处理器通过编码同时处理以下两个响应：</p>

<pre><code>function handleResponse(response) {
  if (response.result.context == "bart") {
    // 更新页面中的 "Bart" 部分。
  } else if (response.result.context == "lisa") {
    // 更新页面中的 "Lisa" 部分。
  }
}
</code></pre>

<h3>
<a id="user-content-id" class="anchor" href="#id" aria-hidden="true"><span class="octicon octicon-link"></span></a>id</h3>

<pre><code>属性值类型: 字符串(string)
父节点: -
</code></pre>

<p>服务提供用于识别响应的标识(无论请求是成功还是有错误)。这对于将服务日志和单独收到的响应对应起来很有用。</p>

<p>示例：</p>

<pre><code>{ "id": "1" }
</code></pre>

<h3>
<a id="user-content-method" class="anchor" href="#method" aria-hidden="true"><span class="octicon octicon-link"></span></a>method</h3>

<pre><code>属性值类型: 字符串(string)
父节点: -
</code></pre>

<p>表示对数据即将执行，或已被执行的操作。在JSON请求的情况下，<em>method</em>属性可以用来指明对数据进行何种操作。在JSON响应的情况下，<em>method</em>属性表明对数据进行了何种操作。</p>

<p>一个JSON-RPC请求的例子，其中<em>method</em>属性表示要在<em>params</em>上执行的操作：</p>

<pre><code>{
  "method": "people.get",
  "params": {
    "userId": "@me",
    "groupId": "@self"
  }
}
</code></pre>

<h3>
<a id="user-content-params" class="anchor" href="#params" aria-hidden="true"><span class="octicon octicon-link"></span></a>params</h3>

<pre><code>属性值类型: 对象(object)
父节点: -
</code></pre>

<p>这个对象作为输入参数的映射发送给RPC请求。它可以和<em>method</em>属性一起用来执行RPC功能。若RPC方法不需要参数，则可以省略该属性。</p>

<p>示例：</p>

<pre><code>{
  "method": "people.get",
  "params": {
    "userId": "@me",
    "groupId": "@self"
  }
}
</code></pre>

<h3>
<a id="user-content-data" class="anchor" href="#data" aria-hidden="true"><span class="octicon octicon-link"></span></a>data</h3>

<pre><code>属性值类型: 对象(object)
父节点: -
</code></pre>

<p>包含响应的所有数据。该属性本身拥有许多保留属性名，下面会有相应的说明。服务可以自由地将自己的数据添加到这个对象。一个JSON响应要么应当包含一个<em>data</em>对象，要么应当包含<em>error</em>对象，但不能两者都包含。如果<em>data</em>和<em>error</em>同时出现，则<em>error</em>对象优先。</p>

<h3>
<a id="user-content-error" class="anchor" href="#error" aria-hidden="true"><span class="octicon octicon-link"></span></a>error</h3>

<pre><code>属性值类型: 对象(object)
父节点: -
</code></pre>

<p>表明错误发生，提供错误的详细信息。错误的格式支持从服务返回一个或多个错误。一个JSON响应可以有一个<em>data</em>对象或者一个<em>error</em>对象，但不能两者都包含。如果<em>data</em>和<em>error</em>都出现，<em>error</em>对象优先。</p>

<p>示例：</p>

<pre><code>{
  "apiVersion": "2.0",
  "error": {
    "code": 404,
    "message": "File Not Found",
    "errors": [{
      "domain": "Calendar",
      "reason": "ResourceNotFoundException",
      "message": "File Not Found
    }]
  }
}
</code></pre>

<h2>
<a id="user-content-data对象的保留属性名" class="anchor" href="#data%E5%AF%B9%E8%B1%A1%E7%9A%84%E4%BF%9D%E7%95%99%E5%B1%9E%E6%80%A7%E5%90%8D" aria-hidden="true"><span class="octicon octicon-link"></span></a>data对象的保留属性名</h2>

<p>JSON对象的<em>data</em>属性可能包含以下属性。</p>

<h3>
<a id="user-content-datakind" class="anchor" href="#datakind" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.kind</h3>

<pre><code>属性值类型: 字符串(sting)
父节点: data
</code></pre>

<p><em>kind</em>属性是对某个特定的对象存储何种类型的信息的指南。可以把它放在<em>data</em>层次，或<em>items</em>的层次，或其它任何有助于区分各类对象的对象中。如果<em>kind</em>对象被提供，它应该是对象的第一个属性（详见下面的<em>属性顺序</em>部分）。</p>

<p>示例：</p>

<pre><code>// "Kind" indicates an "album" in the Picasa API.
{"data": {"kind": "album"}}
</code></pre>

<h3>
<a id="user-content-datafields" class="anchor" href="#datafields" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.fields</h3>

<pre><code>属性值类型: 字符串(string)
父节点: data
</code></pre>

<p>表示做了部分GET之后响应中出现的字段，或做了部分PATCH之后出现在请求中的字段。该属性仅在做了部分GET请求/批处理时存在，且不能为空。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "kind": "user",
    "fields": "author,id",
    "id": "bart",
    "author": "Bart"
  }
}   
</code></pre>

<h3>
<a id="user-content-dataetag" class="anchor" href="#dataetag" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.etag</h3>

<pre><code>属性值类型: 字符串(string)
父节点: data
</code></pre>

<p>响应时提供etag。关于GData APIs中的ETags详情可以在这里找到：<a href="http://code.google.com/apis/gdata/docs/2.0/reference.html#ResourceVersioning">http://code.google.com/apis/gdata/docs/2.0/reference.html#ResourceVersioning</a></p>

<p>示例：</p>

<pre><code>{"data": {"etag": "W/"C0QBRXcycSp7ImA9WxRVFUk.""}}
</code></pre>

<h3>
<a id="user-content-dataid" class="anchor" href="#dataid" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.id</h3>

<pre><code>属性值类型: 字符串(string)
父节点: data
</code></pre>

<p>一个全局唯一标识符用于引用该对象。<em>id</em>属性的具体细节都留给了服务。</p>

<p>示例：</p>

<pre><code>{"data": {"id": "12345"}}
</code></pre>

<h3>
<a id="user-content-datalang" class="anchor" href="#datalang" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.lang</h3>

<pre><code>属性值类型: 字符串(string)(格式由BCP 47指定)
父节点: data (或任何子元素)
</code></pre>

<p>表示该对象内其他属性的语言。该属性模拟HTML的<em>lang</em>属性和XML的<em>xml:lang</em>属性。值应该时BCP 47中定义的一种语言值。如果一个单一的JSON对象包含的数据有多种语言，服务负责制定和标明的lang属性的适当位置。</p>

<p>示例：</p>

<pre><code>{"data": {
  "items": [
    { "lang": "en",
      "title": "Hello world!" },
    { "lang": "fr",
      "title": "Bonjour monde!" }
  ]}
}
</code></pre>

<h3>
<a id="user-content-dataupdated" class="anchor" href="#dataupdated" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.updated</h3>

<pre><code>属性值类型: 字符串(string)(格式由RFC 3339指定)
父节点: data
</code></pre>

<p>指明条目更新的最后日期/时间(RFC 3339)，由服务规定。</p>

<p>示例：</p>

<pre><code>{"data": {"updated": "2007-11-06T16:34:41.000Z"}}
</code></pre>

<h3>
<a id="user-content-datadeleted" class="anchor" href="#datadeleted" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.deleted</h3>

<pre><code>属性值类型: 布尔(boolean)
父节点: data (或任何子元素)
</code></pre>

<p>一个标记元素，当出现时，表示包含的条目已被删除。如果提供了删除属性，它的值必须为<em>true</em>;为<em>false</em>会导致混乱，应该避免。</p>

<p>示例：</p>

<pre><code>{"data": {
  "items": [
    { "title": "A deleted entry",
      "deleted": true
    }
  ]}
}
</code></pre>

<h3>
<a id="user-content-dataitems" class="anchor" href="#dataitems" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.items</h3>

<pre><code>属性值类型: 数组(array)
父节点: data
</code></pre>

<p>属性名<em>items</em>被保留用作表示一组条目(例如,Picasa中的图片，YouTube中的视频)。这种结构的目的是给与当前结果相关的集合提供一个标准位置。例如，知道页面上的<em>items</em>是数组，JSON输出便可能插入一个通用的分页系统。如果<em>items</em>存在，它应该是<em>data</em>对象的最后一个属性。（详见下面的<em>属性顺序</em>部分）。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "items": [
      { /* Object #1 */ },
      { /* Object #2 */ },
      ...
    ]
  }
}
</code></pre>

<h2>
<a id="user-content-用于分页的保留属性名" class="anchor" href="#%E7%94%A8%E4%BA%8E%E5%88%86%E9%A1%B5%E7%9A%84%E4%BF%9D%E7%95%99%E5%B1%9E%E6%80%A7%E5%90%8D" aria-hidden="true"><span class="octicon octicon-link"></span></a>用于分页的保留属性名</h2>

<p>下面的属性位于<em>data</em>对象中，用来给一列数据分页。一些语言和概念是从OpenSearch规范中借鉴过来的。</p>

<p>下面的分页数据允许各种风格的分页，包括：</p>

<ul>
<li>上一页/下一页 - 允许用户在列表中前进和后退，一次一页。<em>nextLink</em> 和<em>previousLink</em>属性 (下面的"链接保留属性名"部分有描述) 用于这种风格的分页。</li>
<li>基于索引的分页 - 允许用户直接跳到条目列表的某个条目位置。例如，要从第200个条目开始载入10个新的条目，开发者可以给用户提供一个URL的查询字符串<em>?startIndex=200</em>。</li>
<li>基于页面的分页 - 允许用户直接跳到条目内的具体页。这跟基于索引的分页很类似,但节省了开发者额外的步骤，不需再为新一页的条目计算条目索引。例如，开发人员可以直接跳到第20页，而不是跳到第200条条目。基于页面分页的网址，可以使用查询字符串<em>?page=1</em>或<em>?page=20</em>。<em>pageIndex</em>和 <em>totalPages</em> 属性用作这种风格的分页. </li>
</ul>

<p>在这份指南的最后可以找到如何使用这些属性来实现分页的例子。</p>

<h3>
<a id="user-content-datacurrentitemcount" class="anchor" href="#datacurrentitemcount" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.currentItemCount</h3>

<pre><code>属性值类型: 整数(integer)
父节点: data
</code></pre>

<p>结果集中的条目数目。应该与items.length相等，并作为一个便利属性提供。例如，假设开发者请求一组搜索条目，并且要求每页10条。查询集共有14条。第一个条目页将会有10个条目，因此<em>itemsPerPage</em>和<em>currentItemCount</em>都应该等于10。下一页的条目还剩下4条；<em>itemsPerPage</em>仍然是10,但是<em>currentItemCount</em>是4.</p>

<p>示例：</p>

<pre><code>{
  "data": {
    // "itemsPerPage" 不需要与 "currentItemCount" 匹配
    "itemsPerPage": 10,
    "currentItemCount": 4
  }
}
</code></pre>

<h3>
<a id="user-content-dataitemsperpage" class="anchor" href="#dataitemsperpage" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.itemsPerPage</h3>

<pre><code>属性值类型: 整数(integer)
父节点: data
</code></pre>

<p>items结果的数目。未必是data.items数组的大小；如果我们查看的是最后一页，data.items的大小可能小于<em>itemsPerPage</em>。但是，data.items的大小不应超过<em>itemsPerPage</em>。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "itemsPerPage": 10
  }
}
</code></pre>

<h3>
<a id="user-content-datastartindex" class="anchor" href="#datastartindex" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.startIndex</h3>

<pre><code>属性值类型: 整数(integer)
父节点: data
</code></pre>

<p>data.items中第一个条目的索引。为了一致，<em>startIndex</em>应从1开始。例如，第一组items中第一条的<em>startIndex</em>应该是1。如果用户请求下一组数据，<em>startIndex</em>可能是10。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "startIndex": 1
  }
}
</code></pre>

<h3>
<a id="user-content-datatotalitemsx" class="anchor" href="#datatotalitemsx" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.totalItemsx</h3>

<pre><code>属性值类型: 整数(integer)
父节点: data
</code></pre>

<p>当前集合中可用的总条目数。例如，如果用户有100篇博客文章，响应可能只包含10篇，但是<em>totalItems</em>应该是100。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "totalItems": 100
  }
}
</code></pre>

<h3>
<a id="user-content-datapaginglinktemplate" class="anchor" href="#datapaginglinktemplate" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.pagingLinkTemplate</h3>

<pre><code>属性值类型: 字符串(string)
父节点: data
</code></pre>

<p>URL模板指出用户可以如何计算随后的分页链接。URL模板中也包含一些保留变量名：表示要载入的条目的<em>{index}</em>，和要载入的页面的<em>{pageIndex}</em>。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "pagingLinkTemplate": "http://www.google.com/search/hl=en&amp;q=chicago+style+pizza&amp;start={index}&amp;sa=N"
  }
}
</code></pre>

<h3>
<a id="user-content-datapageindex" class="anchor" href="#datapageindex" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.pageIndex</h3>

<pre><code>属性值类型: 整数(integer)
父节点: data
</code></pre>

<p>条目的当前页索引。为了一致，<em>pageIndex</em>应从1开始。例如，第一页的<em>pageIndex</em>是1。<em>pageIndex</em>也可以通过基于条目的分页而计算出来<em>pageIndex = floor(startIndex / itemsPerPage) + 1</em>。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "pageIndex": 1
  }
}
</code></pre>

<h3>
<a id="user-content-datatotalpages" class="anchor" href="#datatotalpages" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.totalPages</h3>

<pre><code>属性值类型: 整数(integer)
父节点: data
</code></pre>

<p>当前结果集中的总页数。<em>totalPages</em>也可以通过上面基于条目的分页属性计算出来: <em>totalPages = ceiling(totalItems / itemsPerPage).</em>。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "totalPages": 50
  }
}
</code></pre>

<h2>
<a id="user-content-用于链接的保留属性名" class="anchor" href="#%E7%94%A8%E4%BA%8E%E9%93%BE%E6%8E%A5%E7%9A%84%E4%BF%9D%E7%95%99%E5%B1%9E%E6%80%A7%E5%90%8D" aria-hidden="true"><span class="octicon octicon-link"></span></a>用于链接的保留属性名</h2>

<p>下面的属性位于<em>data</em>对象中，用来表示对其他资源的引用。有两种形式的链接属性：1）对象，它可以包含任何种类的引用（比如JSON-RPC对象），2)URL字符串，表示资源的URIs(后缀总为'Link')。</p>

<h3>
<a id="user-content-dataself--dataselflink" class="anchor" href="#dataself--dataselflink" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.self / data.selfLink</h3>

<pre><code>属性值类型: 对象(object)/字符串(string)
父节点: data
</code></pre>

<p>自身链接可以用于取回条目数据。比如，在用户的Picasa相册中，条目中的每个相册对象都会包含一个<em>selfLink</em>用于检索这个相册的相关数据。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "self": { },
    "selfLink": "http://www.google.com/feeds/album/1234"
  }
}
</code></pre>

<h3>
<a id="user-content-dataedit--dataeditlink" class="anchor" href="#dataedit--dataeditlink" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.edit / data.editLink</h3>

<pre><code>属性值类型: 对象(object)/字符串(string)
父节点: data
</code></pre>

<p>编辑链接表明用户可以发送更新或删除请求。这对于REST风格的APIs很有用。该链接仅在用户能够更新和删除该条目时提供。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "edit": { },
    "editLink": "http://www.google.com/feeds/album/1234/edit"
  }
}
</code></pre>

<h3>
<a id="user-content-datanext--datanextlink" class="anchor" href="#datanext--datanextlink" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.next / data.nextLink</h3>

<pre><code>属性值类型: 对象(object)/字符串(string)
父节点: data
</code></pre>

<p>该下一页链接标明如何取得更多数据。它指明载入下一组数据的位置。它可以同<em>itemsPerPage</em>，<em>startIndex</em> 和 <em>totalItems</em> 属性一起使用用于分页数据。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "next": { },
    "nextLink": "http://www.google.com/feeds/album/1234/next"
  }
}
</code></pre>

<h3>
<a id="user-content-dataprevious--datapreviouslink" class="anchor" href="#dataprevious--datapreviouslink" aria-hidden="true"><span class="octicon octicon-link"></span></a>data.previous / data.previousLink</h3>

<pre><code>属性值类型: 对象(object)/字符串(string)
父节点: data
</code></pre>

<p>该上一页链接标明如何取得更多数据。它指明载入上一组数据的位置。它可以连同<em>itemsPerPage</em>，<em>startIndex</em> 和 <em>totalItems</em>  属性用于分页数据。</p>

<p>示例：</p>

<pre><code>{
  "data": {
    "previous": { },
    "previousLink": "http://www.google.com/feeds/album/1234/next"
  }
}
</code></pre>

<h2>
<a id="user-content-错误对象中的保留属性名" class="anchor" href="#%E9%94%99%E8%AF%AF%E5%AF%B9%E8%B1%A1%E4%B8%AD%E7%9A%84%E4%BF%9D%E7%95%99%E5%B1%9E%E6%80%A7%E5%90%8D" aria-hidden="true"><span class="octicon octicon-link"></span></a>错误对象中的保留属性名</h2>

<p>JSON对象的<em>error</em>属性应包含以下属性。</p>

<h3>
<a id="user-content-errorcode" class="anchor" href="#errorcode" aria-hidden="true"><span class="octicon octicon-link"></span></a>error.code</h3>

<pre><code>属性值类型: 整数(integer)
父节点: error
</code></pre>

<p>表示该错误的编号。这个属性通常表示HTTP响应码。如果存在多个错误，<em>code</em>应为第一个出错的错误码。</p>

<p>示例：</p>

<pre><code>{
  "error":{
    "code": 404
  }
}
</code></pre>

<h3>
<a id="user-content-errormessage" class="anchor" href="#errormessage" aria-hidden="true"><span class="octicon octicon-link"></span></a>error.message</h3>

<pre><code>属性值类型: 字符串(string)
父节点: error
</code></pre>

<p>一个人类可读的信息，提供有关错误的详细信息。如果存在多个错误，<em>message</em>应为第一个错误的错误信息。</p>

<p>示例：</p>

<pre><code>{
  "error":{
    "message": "File Not Found"
  }
}   
</code></pre>

<h3>
<a id="user-content-errorerrors" class="anchor" href="#errorerrors" aria-hidden="true"><span class="octicon octicon-link"></span></a>error.errors</h3>

<pre><code>属性值类型: 数组(array)
父节点: error
</code></pre>

<p>包含关于错误的附加信息。如果服务返回多个错误。<em>errors</em>数组中的每个元素表示一个不同的错误。</p>

<p>示例：</p>

<pre><code>{ "error": { "errors": [] } }   
</code></pre>

<h3>
<a id="user-content-errorerrorsdomain" class="anchor" href="#errorerrorsdomain" aria-hidden="true"><span class="octicon octicon-link"></span></a>error.errors[].domain</h3>

<pre><code>属性值类型: 字符串(string)
父节点: error.errors
</code></pre>

<p>服务抛出该错误的唯一识别符。它帮助区分服务的从普通协议错误(如,找不到文件)中区分出具体错误(例如，给日历插入事件的错误)。</p>

<p>示例：</p>

<pre><code>{
  "error":{
    "errors": [{"domain": "Calendar"}]
  }
}
</code></pre>

<h3>
<a id="user-content-errorerrorsreason" class="anchor" href="#errorerrorsreason" aria-hidden="true"><span class="octicon octicon-link"></span></a>error.errors[].reason</h3>

<pre><code>属性值类型: 字符串(string)
父节点: error.errors
</code></pre>

<p>该错误的唯一识别符。不同于<em>error.code</em>属性，它不是HTTP响应码。</p>

<p>示例：</p>

<pre><code>{
  "error":{
    "errors": [{"reason": "ResourceNotFoundException"}]
  }
}
</code></pre>

<h3>
<a id="user-content-errorerrorsmessage" class="anchor" href="#errorerrorsmessage" aria-hidden="true"><span class="octicon octicon-link"></span></a>error.errors[].message</h3>

<pre><code>属性值类型: 字符串(string)
父节点: error.errors
</code></pre>

<p>一个人类可读的信息，提供有关错误的更多细节。如果只有一个错误，该字段应该与<em>error.message</em>匹配。</p>

<p>示例：</p>

<pre><code>{
  "error":{
    "code": 404
    "message": "File Not Found",
    "errors": [{"message": "File Not Found"}]
  }
}       
</code></pre>

<h3>
<a id="user-content-errorerrorslocation" class="anchor" href="#errorerrorslocation" aria-hidden="true"><span class="octicon octicon-link"></span></a>error.errors[].location</h3>

<pre><code>属性值类型: 字符串(string)
父节点: error.errors
</code></pre>

<p>错误发生的位置（根据<em>locationType</em>字段解释该值）。</p>

<p>示例：</p>

<pre><code>{
  "error":{
    "errors": [{"location": ""}]
  }
}
</code></pre>

<h3>
<a id="user-content-errorerrorslocationtype" class="anchor" href="#errorerrorslocationtype" aria-hidden="true"><span class="octicon octicon-link"></span></a>error.errors[].locationType</h3>

<pre><code>属性值类型: 字符串(string)
父节点: error.errors
</code></pre>

<p>标明如何解释<em>location</em>属性。</p>

<p>示例：</p>

<pre><code>{
  "error":{
    "errors": [{"locationType": ""}]
  }
}
</code></pre>

<h3>
<a id="user-content-errorerrorsextendedhelp" class="anchor" href="#errorerrorsextendedhelp" aria-hidden="true"><span class="octicon octicon-link"></span></a>error.errors[].extendedHelp</h3>

<pre><code>属性值类型: 字符串(string)
父节点: error.errors
</code></pre>

<p>help text的URI，使错误更易于理解。</p>

<p>示例：（注：原示例这里有笔误，中文版这里做了校正）</p>

<pre><code>{
  "error":{
    "errors": [{"extendedHelp": "http://url.to.more.details.example.com/"}]
  }
}
</code></pre>

<h3>
<a id="user-content-errorerrorssendreport" class="anchor" href="#errorerrorssendreport" aria-hidden="true"><span class="octicon octicon-link"></span></a>error.errors[].sendReport</h3>

<pre><code>属性值类型: 字符串(string)
父节点: error.errors
</code></pre>

<p>report form的URI，服务用它来收集错误状态的数据。该URL会预先载入描述请求的参数</p>

<p>示例：</p>

<pre><code>{
  "error":{
    "errors": [{"sendReport": "http://report.example.com/"}]
  }
}
</code></pre>

<h2>
<a id="user-content-属性顺序" class="anchor" href="#%E5%B1%9E%E6%80%A7%E9%A1%BA%E5%BA%8F" aria-hidden="true"><span class="octicon octicon-link"></span></a>属性顺序</h2>

<p>在JSON对象中属性可有任意顺序。然而，在某些情况下，有序的属性可以帮助分析器快速解释数据，并带来更好的性能。在移动环境下的解析器就是个例子，在这种情况下，性能和内存是至关重要的，不必要的解析也应尽量避免。</p>

<h3>
<a id="user-content-kind属性" class="anchor" href="#kind%E5%B1%9E%E6%80%A7" aria-hidden="true"><span class="octicon octicon-link"></span></a>Kind属性</h3>

<p><strong>Kind属性应为第一属性</strong></p>

<p>假设一个解析器负责将一个原始JSON流解析成一个特定的对象。<em>kind</em>属性会引导解析器将适合的对象实例化。因而它应该是JSON对象的第一个属性。这仅适用于对象有一个kind属性的情况(通常可以在<em>data</em>和<em>items</em>属性中找到)。</p>

<h3>
<a id="user-content-items属性" class="anchor" href="#items%E5%B1%9E%E6%80%A7" aria-hidden="true"><span class="octicon octicon-link"></span></a>Items属性</h3>

<p><strong><em>items</em>应该是<em>data</em>对象的最后一个属性</strong></p>

<p>这使得阅读每一个具体条目前前已读所有的集合属性。在有很多条目的情况下，这样就避免了开发人员只需要从数据的字段时不必要的解析这些条目。</p>

<p>这让阅读所有集合属性先于阅读单个条目。如遇多个条目的情况，当开发者仅需要数据中的字段时，这就可避免解析不必要的条目。</p>

<p>属性顺序示例：</p>

<pre><code>// "kind" 属性区分 "album" 和 "photo".
// "Kind" 始终是它父对象的第一个属性.
// "items" 属性是 "data" 对象的最后一个属性.
{
  "data": {
    "kind": "album",
    "title": "My Photo Album",
    "description": "An album in the user's account",
    "items": [
      {
        "kind": "photo",
        "title": "My First Photo"
      }
    ]
  }
}
</code></pre>

<h2>
<a id="user-content-示例" class="anchor" href="#%E7%A4%BA%E4%BE%8B" aria-hidden="true"><span class="octicon octicon-link"></span></a>示例</h2>

<h3>
<a id="user-content-youtube-json-api" class="anchor" href="#youtube-json-api" aria-hidden="true"><span class="octicon octicon-link"></span></a>YouTube JSON API</h3>

<p>这是YouTube JSON API响应对象的示例。你可以从中学到更多关于YouTube JSON API的内容：<a href="http://code.google.com/apis/youtube/2.0/developers_guide_jsonc.html">http://code.google.com/apis/youtube/2.0/developers_guide_jsonc.html</a></p>

<pre><code>{
  "apiVersion": "2.0",
  "data": {
    "updated": "2010-02-04T19:29:54.001Z",
    "totalItems": 6741,
    "startIndex": 1,
    "itemsPerPage": 1,
    "items": [
      {
        "id": "BGODurRfVv4",
        "uploaded": "2009-11-17T20:10:06.000Z",
        "updated": "2010-02-04T06:25:57.000Z",
        "uploader": "docchat",
        "category": "Animals",
        "title": "From service dog to SURFice dog",
        "description": "Surf dog Ricochets inspirational video ...",
        "tags": [
          "Surf dog",
          "dog surfing",
          "dog",
          "golden retriever",
        ],
        "thumbnail": {
          "default": "http://i.ytimg.com/vi/BGODurRfVv4/default.jpg",
          "hqDefault": "http://i.ytimg.com/vi/BGODurRfVv4/hqdefault.jpg"
        },
        "player": {
          "default": "http://www.youtube.com/watch?v=BGODurRfVv4&amp;feature=youtube_gdata",
          "mobile": "http://m.youtube.com/details?v=BGODurRfVv4"
        },
        "content": {
          "1": "rtsp://v5.cache6.c.youtube.com/CiILENy73wIaGQn-Vl-0uoNjBBMYDSANFEgGUgZ2aWRlb3MM/0/0/0/video.3gp",
          "5": "http://www.youtube.com/v/BGODurRfVv4?f=videos&amp;app=youtube_gdata",
          "6": "rtsp://v7.cache7.c.youtube.com/CiILENy73wIaGQn-Vl-0uoNjBBMYESARFEgGUgZ2aWRlb3MM/0/0/0/video.3gp"
        },
        "duration": 315,
        "rating": 4.96,
        "ratingCount": 2043,
        "viewCount": 1781691,
        "favoriteCount": 3363,
        "commentCount": 1007,
        "commentsAllowed": true
      }
    ]
  }
}
</code></pre>

<h3>
<a id="user-content-分页示例" class="anchor" href="#%E5%88%86%E9%A1%B5%E7%A4%BA%E4%BE%8B" aria-hidden="true"><span class="octicon octicon-link"></span></a>分页示例</h3>

<p>如何将Google搜索条目作为JSON对象展现出来，对分页变量也有特别关注。</p>

<p>这个示例仅用作说明。下面的API实际上并不存在。</p>

<p>这是Google搜索结果页面的示例：
<a href="https://camo.githubusercontent.com/c8ff0de46d7cb966ddae8b3350960400fdd6962d/687474703a2f2f676f6f676c652d7374796c6567756964652e676f6f676c65636f64652e636f6d2f73766e2f7472756e6b2f6a736f6e637374796c6567756964655f6578616d706c655f30312e706e67" target="_blank"><img src="https://camo.githubusercontent.com/c8ff0de46d7cb966ddae8b3350960400fdd6962d/687474703a2f2f676f6f676c652d7374796c6567756964652e676f6f676c65636f64652e636f6d2f73766e2f7472756e6b2f6a736f6e637374796c6567756964655f6578616d706c655f30312e706e67" alt="image" data-canonical-src="http://google-styleguide.googlecode.com/svn/trunk/jsoncstyleguide_example_01.png" style="max-width:100%;"></a></p>

<p><a href="https://camo.githubusercontent.com/0341a3abf1faaffd6dc67039efd964336d285f54/687474703a2f2f676f6f676c652d7374796c6567756964652e676f6f676c65636f64652e636f6d2f73766e2f7472756e6b2f6a736f6e637374796c6567756964655f6578616d706c655f30322e706e67" target="_blank"><img src="https://camo.githubusercontent.com/0341a3abf1faaffd6dc67039efd964336d285f54/687474703a2f2f676f6f676c652d7374796c6567756964652e676f6f676c65636f64652e636f6d2f73766e2f7472756e6b2f6a736f6e637374796c6567756964655f6578616d706c655f30322e706e67" alt="image" data-canonical-src="http://google-styleguide.googlecode.com/svn/trunk/jsoncstyleguide_example_02.png" style="max-width:100%;"></a></p>

<p>这是该页面JSON形式的呈现：</p>

<pre><code>{
  "apiVersion": "2.1",
  "id": "1",
  "data": {
    "query": "chicago style pizza",
    "time": "0.1",
    "currentItemCount": 10,
    "itemsPerPage": 10,
    "startIndex": 11,
    "totalItems": 2700000,
    "nextLink": "http://www.google.com/search?hl=en&amp;q=chicago+style+pizza&amp;start=20&amp;sa=N"
    "previousLink": "http://www.google.com/search?hl=en&amp;q=chicago+style+pizza&amp;start=0&amp;sa=N",
    "pagingLinkTemplate": "http://www.google.com/search/hl=en&amp;q=chicago+style+pizza&amp;start={index}&amp;sa=N",
    "items": [
      {
        "title": "Pizz'a Chicago Home Page"
        // More fields for the search results
      }
      // More search results
    ]
  }
}
</code></pre>

<p>这是如何展现屏幕截图中的色块的例子（背景颜色对应下图中的颜色）</p>

<ul>
<li>Results 11 - 20 of about 2,700,000 = startIndex</li>
<li>Results 11 - 20 of about 2,700,000 = startIndex + currentItemCount - 1</li>
<li>Results 11 - 20 of about 2,700,000 = totalItems</li>
<li>Search results = items (formatted appropriately)</li>
<li>Previous/Next = previousLink / nextLink</li>
<li>Numbered links in "Gooooooooooogle" = Derived from "pageLinkTemplate". The developer is responsible for calculating the values for {index} and substituting those values into the "pageLinkTemplate". The pageLinkTemplate's {index} variable is calculated as follows:

<ul>
<li>Index #1 = 0 * itemsPerPage = 0</li>
<li>Index #2 = 2 * itemsPerPage = 10</li>
<li>Index #3 = 3 * itemsPerPage = 20</li>
<li>Index #N = N * itemsPerPage</li>
</ul>
</li>
</ul>

<h2>
<a id="user-content-附录" class="anchor" href="#%E9%99%84%E5%BD%95" aria-hidden="true"><span class="octicon octicon-link"></span></a>附录</h2>

<h3>
<a id="user-content-附录ajavascript中的保留字" class="anchor" href="#%E9%99%84%E5%BD%95ajavascript%E4%B8%AD%E7%9A%84%E4%BF%9D%E7%95%99%E5%AD%97" aria-hidden="true"><span class="octicon octicon-link"></span></a>附录A:JavaScript中的保留字</h3>

<p><strong>下列JavaScript保留字应该避免在属性名中使用</strong></p>

<p>下面的但在在JavaScript语言中被保留，不能作为在点访问符中使用。这份名单代表此时的最佳关键字的知识;列表可能会改变或根据您的特定的执行环境更改。</p>

<p>下面是JavaScript语言中的保留字，且不能在点访问符中使用。这份清单集合了当前最新的关键字，该清单可能会根据具体的执行环境而有所变更或改变。</p>

<p>来自<a href="http://www.ecma-international.org/publications/standards/Ecma-262.htm">ECMAScript 语言规范第五版</a></p>

<pre><code>abstract
boolean break byte
case catch char class const continue
debugger default delete do double
else enum export extends
false final finally float for function
goto
if implements import in instanceof int interface
let long
native new null
package private protected public
return
short static super switch synchronized
this throw throws transient true try typeof
var volatile void
while with
yield
</code></pre>

<p>除了特别<a href="http://code.google.com/policies.html">说明</a>，该页面的内容均由<a href="http://creativecommons.org/licenses/by/3.0/">共同创作协议</a>(CC BY 3.0)授权许可，示例代码均由<a href="http://www.apache.org/licenses/LICENSE-2.0">Apache 2.0</a>许可证授权许可）</p>

<p>－EOF-</p>
</article>
  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.06060s from github-fe126-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-5c08de317e4054ec200d36d3b1361ddd3cb30c05c9070a9d72862ee28ab1d7f9.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github/index-bfb27c17548d6c05bbe36a476673446098f04766b4a2ce445e2ae9d5374622ff.js"></script>
      
      

  </body>
</html>

