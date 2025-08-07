// Dashboard JavaScript functionality

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-refresh functionality for build status
    function refreshBuildStatus() {
        const statusElements = document.querySelectorAll('[data-job-id]');
        
        statusElements.forEach(function(element) {
            const jobId = element.getAttribute('data-job-id');
            
            fetch(`/api/job/${jobId}/status/`)
                .then(response => response.json())
                .then(data => {
                    if (data.latest_build) {
                        updateBuildStatus(element, data.latest_build);
                    }
                })
                .catch(error => {
                    console.error('Error fetching build status:', error);
                });
        });
    }

    function updateBuildStatus(element, buildData) {
        const statusBadge = element.querySelector('.build-status');
        if (statusBadge) {
            // Update status badge
            statusBadge.className = `badge bg-${getStatusColor(buildData.status)}`;
            statusBadge.textContent = `#${buildData.build_number}`;
            
            // Update timestamp
            const timestamp = element.querySelector('.build-timestamp');
            if (timestamp) {
                timestamp.textContent = formatTimestamp(buildData.started_at);
            }
        }
    }

    function getStatusColor(status) {
        const colors = {
            'success': 'success',
            'failed': 'danger',
            'running': 'warning',
            'pending': 'secondary',
            'aborted': 'dark'
        };
        return colors[status] || 'secondary';
    }

    function formatTimestamp(timestamp) {
        const date = new Date(timestamp);
        const now = new Date();
        const diffMs = now - date;
        const diffMins = Math.floor(diffMs / 60000);
        
        if (diffMins < 1) return 'Just now';
        if (diffMins < 60) return `${diffMins}m ago`;
        
        const diffHours = Math.floor(diffMins / 60);
        if (diffHours < 24) return `${diffHours}h ago`;
        
        const diffDays = Math.floor(diffHours / 24);
        return `${diffDays}d ago`;
    }

    // Build log functionality
    function loadBuildLog(buildId) {
        const logContainer = document.getElementById('build-log-content');
        if (!logContainer) return;

        logContainer.innerHTML = '<div class="text-center"><div class="loading-spinner"></div> Loading log...</div>';

        fetch(`/api/build/${buildId}/log/`)
            .then(response => response.json())
            .then(data => {
                logContainer.innerHTML = `<pre class="build-log">${escapeHtml(data.log_output)}</pre>`;
                // Auto-scroll to bottom
                logContainer.scrollTop = logContainer.scrollHeight;
            })
            .catch(error => {
                logContainer.innerHTML = '<div class="text-danger">Error loading build log</div>';
                console.error('Error fetching build log:', error);
            });
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Progress bar animations
    function animateProgressBars() {
        const progressBars = document.querySelectorAll('.progress-bar');
        progressBars.forEach(function(bar) {
            const width = bar.style.width;
            bar.style.width = '0%';
            setTimeout(function() {
                bar.style.width = width;
                bar.style.transition = 'width 1s ease-in-out';
            }, 100);
        });
    }

    // Initialize progress bar animations
    animateProgressBars();

    // Refresh build status every 30 seconds (only if not in a modal)
    setInterval(function() {
        if (!document.querySelector('.modal.show')) {
            refreshBuildStatus();
        }
    }, 30000);

    // Handle build log modal
    const buildLogModal = document.getElementById('buildLogModal');
    if (buildLogModal) {
        buildLogModal.addEventListener('show.bs.modal', function(event) {
            const button = event.relatedTarget;
            const buildId = button.getAttribute('data-build-id');
            if (buildId) {
                loadBuildLog(buildId);
            }
        });
    }

    // Handle search functionality
    const searchInput = document.getElementById('job-search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const jobRows = document.querySelectorAll('.job-row');
            
            jobRows.forEach(function(row) {
                const jobName = row.querySelector('.job-name').textContent.toLowerCase();
                const jobDescription = row.querySelector('.job-description');
                const description = jobDescription ? jobDescription.textContent.toLowerCase() : '';
                
                if (jobName.includes(searchTerm) || description.includes(searchTerm)) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    }

    // Handle filter functionality
    const statusFilter = document.getElementById('status-filter');
    if (statusFilter) {
        statusFilter.addEventListener('change', function() {
            const selectedStatus = this.value;
            const jobRows = document.querySelectorAll('.job-row');
            
            jobRows.forEach(function(row) {
                const statusBadge = row.querySelector('.status-badge');
                const status = statusBadge ? statusBadge.textContent.toLowerCase() : '';
                
                if (selectedStatus === '' || status.includes(selectedStatus.toLowerCase())) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

